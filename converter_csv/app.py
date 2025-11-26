# -*- coding: utf-8 -*-
"""
Converter CSV by LimberDuck (pronounced *ˈlɪm.bɚ dʌk*) is a GUI
tool which lets you convert multiple large csv files to xlsx files.
Copyright (C) 2018 Damian Krawczyk

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import datetime
import glob
import os
import time
import csv
import traceback
import xlsxwriter
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from converter_csv import utilities, ldcc_ico
from converter_csv.ui import mainwindow
import sys
import subprocess
import platform
from converter_csv.dialogs import about
from converter_csv.dialogs import update_check
from converter_csv.dialogs import url_open
from converter_csv import __about__
import requests
from packaging import version
from converter_csv import __about__


class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.__files_to_pars = []
        self.__delimiter = ""
        self.__parsing_settings = {}
        self.__target_directory = ""
        self.__target_directory_changed = False
        self.__file_conversion_counter = 0
        self.__suffix = ""
        self.update_parsing_settings("suffix", self.__suffix)
        self.__suffix_template = ""
        self.update_parsing_settings("suffix_template", self.__suffix_template)

        self.parsing_thread = ParsingThread(
            files_to_pars=self.__files_to_pars,
            target_directory=self.__target_directory,
            target_directory_changed=self.__target_directory_changed,
            parsing_settings=self.__parsing_settings,
        )

        self.actionOpen_file.triggered.connect(self.open_files)
        self.actionOpen_directory.triggered.connect(self.open_directory)
        self.actionExit.triggered.connect(self.exit_application)
        self.actionStart_conversion.triggered.connect(self.parsing_thread_start)
        self.actionChange_separator.triggered.connect(self.change_delimiter)
        self.actionChange_target_directory.triggered.connect(
            self.change_target_directory
        )
        self.actionOpen_target_directory.triggered.connect(self.open_target_directory)
        self.actionAbout.triggered.connect(self.open_dialog_about)
        self.actionCheck_for_Update.triggered.connect(self.open_dialog_update_check)
        self.actionCheck_Announcements.triggered.connect(
            self.check_announcements_button
        )
        self.actionDocumentation.triggered.connect(self.open_url_documentation)
        self.actionGitHub.triggered.connect(self.open_url_github)
        self.actionReleases.triggered.connect(self.open_url_github_releases)
        self.checkBox_suffix_timestamp.stateChanged.connect(
            self.suffix_timestamp_changed
        )

        self.checkBox_suffix_custom.stateChanged.connect(self.suffix_custom_changed)
        self.lineEdit_suffix_custom_value.textChanged.connect(
            self.suffix_custom_changed
        )
        self.checkBox_auto_detect_separator.stateChanged.connect(
            self.auto_detect_separator_changed
        )
        # Match any character but \/:*?"<>|
        reg_ex = QRegExp('[^\\\\/:*?"<>|]+')
        line_edit_suffix_custom_value_validator = QRegExpValidator(
            reg_ex, self.lineEdit_suffix_custom_value
        )
        self.lineEdit_suffix_custom_value.setValidator(
            line_edit_suffix_custom_value_validator
        )

        self.pushButton_start.clicked.connect(self.parsing_thread_start)
        self.pushButton_separator_change.clicked.connect(self.change_delimiter)
        self.pushButton_target_dir_change.clicked.connect(self.change_target_directory)
        self.pushButton_target_dir_open.clicked.connect(self.open_target_directory)

        self.checkBox_suffix_timestamp.setChecked(True)
        self.checkBox_auto_detect_separator.setChecked(True)
        self.pushButton_start.setDisabled(True)
        self.progressBar.setHidden(True)

        target_dir = os.path.expanduser("~")
        self.set_target_directory(target_dir)
        self.get_target_directory_from_file()

        files = sys.argv[1:]
        if len(files) > 0:
            self.list_of_files_to_pars(files)
            self.pushButton_start.setEnabled(True)

            source_file_path = os.path.dirname(os.path.abspath(files[0]))
            self.set_target_directory(source_file_path)
            self.get_target_directory_from_file()

        self.set_delimiter(",")
        self.get_delimiter()

        # Initialize auto-detect separator setting
        self.update_parsing_settings("auto_detect_separator", True)

        self.print_log(
            "If you don't know how to use particular options "
            "hover mouse pointer on option for which you have any doubts to see tooltip. "
            "Hover mouse pointer here, to see tooltip for progress preview.",
            "red",
        )

        self.check_announcements()

        self.progressBar.setRange(0, 10)

        # Enable drag and drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        """
        Function handles drag enter event to accept file and directory drops.

        :param event: QDragEnterEvent
        """
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        """
        Function handles drop event to process dropped files and directories.

        Supports dropping:
        - One or more CSV files
        - One or more directories containing CSV files

        :param event: QDropEvent
        """
        if not event.mimeData().hasUrls():
            return

        urls = event.mimeData().urls()
        files_to_process = []
        directories_to_process = []

        # Separate files and directories
        for url in urls:
            # Convert QUrl to local file path
            file_path = url.toLocalFile()

            if not file_path:
                continue

            # Check if it's a directory or file
            if os.path.isdir(file_path):
                directories_to_process.append(file_path)
            elif os.path.isfile(file_path):
                # Check if it's a CSV file
                if file_path.lower().endswith(".csv"):
                    files_to_process.append(file_path)

        # Process directories (recursively find CSV files)
        if directories_to_process:
            info = "Files from directory and subdirectories opening via drag and drop."
            color = "black"
            self.print_log(info, color=color)

            extension = "*.csv"
            os_separator = os.path.sep

            # Set target directory to the first dropped directory (only once)
            if not self.__target_directory_changed:
                self.set_target_directory(directories_to_process[0])
                self.get_target_directory_from_directory()

            for directory in directories_to_process:
                # Find all CSV files recursively
                csv_files = glob.glob(
                    directory + os_separator + "**" + os_separator + extension,
                    recursive=True,
                )
                files_to_process.extend(csv_files)

        # Process files
        if files_to_process:
            info = "File\\-s opening via drag and drop."
            color = "black"
            self.print_log(info, color=color)

            # Set target directory to the first file's directory if not changed
            if files_to_process and not self.__target_directory_changed:
                target_directory2 = os.path.dirname(
                    os.path.abspath(files_to_process[0])
                )
                self.set_target_directory(target_directory2)
                self.get_target_directory_from_file()

            self.list_of_files_to_pars(files_to_process)
            self.pushButton_start.setEnabled(True)
            self.__target_directory_changed = False
        else:
            info = "No CSV files found in dropped items."
            color = "red"
            self.print_log(info, color=color)

        event.acceptProposedAction()

    def suffix_timestamp_changed(self):
        """
        Function sets suffix appropriately if checkBox_suffix_timestamp has changed.
        """
        if (
            self.checkBox_suffix_timestamp.isChecked()
            and not self.checkBox_suffix_custom.isChecked()
        ):
            time_now = datetime.datetime.now()
            time_now_formatted = time_now.strftime("%Y-%m-%d_%H%M%S")
            self.change_suffix("_" + time_now_formatted)
            self.__suffix_template = "suffix_timestamp"

        elif (
            not self.checkBox_suffix_timestamp.isChecked()
            and self.checkBox_suffix_custom.isChecked()
        ):
            suffix_custom_value = self.lineEdit_suffix_custom_value.text()
            if suffix_custom_value:
                space = "_"
                self.__suffix_template = "suffix_custom"
            else:
                space = ""
                self.__suffix_template = "suffix_custom_empty"
            self.change_suffix(space + suffix_custom_value)

        elif (
            self.checkBox_suffix_timestamp.isChecked()
            and self.checkBox_suffix_custom.isChecked()
        ):
            time_now = datetime.datetime.now()
            time_now_formatted = time_now.strftime("%Y-%m-%d_%H%M%S")
            suffix_custom_value = self.lineEdit_suffix_custom_value.text()
            if suffix_custom_value:
                space = "_"
                self.__suffix_template = "suffix_custom_timestamp"
            else:
                space = ""
                self.__suffix_template = "suffix_custom_empty_timestamp"
            self.change_suffix(space + suffix_custom_value + "_" + time_now_formatted)

        else:
            self.change_suffix("")
            self.__suffix_template = "empty"

    def suffix_custom_changed(self):
        """
        Function sets suffix appropriately if checkBox_suffix_custom has changed.
        """
        if (
            self.checkBox_suffix_custom.isChecked()
            and not self.checkBox_suffix_timestamp.isChecked()
        ):
            suffix_custom_value = self.lineEdit_suffix_custom_value.text()
            if suffix_custom_value:
                space = "_"
                self.__suffix_template = "suffix_custom"
            else:
                space = ""
                self.__suffix_template = "suffix_custom_empty"
            self.change_suffix(space + suffix_custom_value)

        elif (
            not self.checkBox_suffix_custom.isChecked()
            and self.checkBox_suffix_timestamp.isChecked()
        ):
            time_now = datetime.datetime.now()
            time_now_formatted = time_now.strftime("%Y-%m-%d_%H%M%S")
            self.change_suffix("_" + time_now_formatted)
            self.__suffix_template = "suffix_timestamp"

        elif (
            self.checkBox_suffix_custom.isChecked()
            and self.checkBox_suffix_timestamp.isChecked()
        ):
            time_now = datetime.datetime.now()
            time_now_formatted = time_now.strftime("%Y-%m-%d_%H%M%S")
            suffix_custom_value = self.lineEdit_suffix_custom_value.text()
            if suffix_custom_value:
                space = "_"
                self.__suffix_template = "suffix_timestamp_custom"
            else:
                space = ""
                self.__suffix_template = "suffix_timestamp_custom_empty"
            self.change_suffix("_" + time_now_formatted + space + suffix_custom_value)

        else:
            self.change_suffix("")
            self.__suffix_template = "empty"

    def open_dialog_about(self):
        """
        Function opens About dialog.
        """
        self.dialog_about = about.About()

    def open_dialog_update_check(self):
        """
        Function opens Update check dialog.
        """
        self.dialog_update_check = update_check.UpdateCheck()

    def check_announcements(self):
        """
        Function checks Announcements.
        """

        announcements = utilities.get_announcements(
            __about__.__package_name__, __about__.__version__
        )
        for a in announcements:
            self.print_log(
                f"[{a['type'].upper()}] {a['title']}: {a['message']}", "orange"
            )

    def check_announcements_button(self):
        """
        Function checks Announcements.
        """

        announcements = utilities.get_announcements(
            __about__.__package_name__, __about__.__version__
        )
        for a in announcements:
            self.print_log(
                f"[{a['type'].upper()}] {a['title']}: {a['message']}", "orange"
            )

        if not announcements:
            self.print_log("No new announcements.", "green")

    def display_update_window(self):
        """
        Function automatically opens Update check dialog if new version is available.
        """

        PACKAGE_NAME = __about__.__package_name__
        current_version = __about__.__version__

        try:
            response = requests.get(
                f"https://pypi.org/pypi/{PACKAGE_NAME}/json", timeout=1.5
            )
            response.raise_for_status()
            latest = response.json()["info"]["version"]
            if version.parse(latest) > version.parse(current_version):
                print("New version available:", latest)
                self.dialog_update_check = update_check.UpdateCheck()

        except requests.exceptions.ConnectionError as e:
            return (
                None,
                f"Could not check for updates: <br><br><i>Connection error</i><br><br>{e}",
            )
        except Exception as e:
            return None, f"Could not check for updates:<br><br>{e}"

    def open_url_documentation(self):
        """
        Function opens Url with documentation.
        """
        PACKAGE_NAME = __about__.__package_name__
        url_open.open_website(f"https://limberduck.org/en/latest/tools/{PACKAGE_NAME}/")

    def open_url_github(self):
        """
        Function opens Url with GitHub.
        """
        PACKAGE_NAME = __about__.__package_name__
        url_open.open_website(f"https://github.com/LimberDuck/{PACKAGE_NAME}")

    def open_url_github_releases(self):
        """
        Function opens Url with GitHub Releases.
        """
        PACKAGE_NAME = __about__.__package_name__
        url_open.open_website(f"https://github.com/LimberDuck/{PACKAGE_NAME}/releases")

    def parsing_thread_start(self):
        """
        Function starts separate thread to pars selected files.
        """
        self.__file_conversion_counter = 0
        self.statusbar.clearMessage()
        self.progressBar.setVisible(True)

        info = "Converting started:"
        color = "black"
        self.print_log(info, color=color)
        try:
            if self.__suffix_template == "suffix_timestamp":
                time_now = datetime.datetime.now()
                time_now_formatted = time_now.strftime("%Y%m%d_%H%M%S")
                self.update_parsing_settings("suffix", "_" + time_now_formatted)

            elif self.__suffix_template == "suffix_custom":
                suffix_custom_value = self.lineEdit_suffix_custom_value.text()
                self.update_parsing_settings("suffix", "_" + suffix_custom_value)

            elif self.__suffix_template == "suffix_custom_empty":
                self.update_parsing_settings("suffix", "")

            elif self.__suffix_template == "suffix_custom_timestamp":
                time_now = datetime.datetime.now()
                time_now_formatted = time_now.strftime("%Y%m%d_%H%M%S")
                suffix_custom_value = self.lineEdit_suffix_custom_value.text()
                self.update_parsing_settings(
                    "suffix", "_" + suffix_custom_value + "_" + time_now_formatted
                )

            elif self.__suffix_template == "suffix_custom_empty_timestamp":
                time_now = datetime.datetime.now()
                time_now_formatted = time_now.strftime("%Y%m%d_%H%M%S")
                self.update_parsing_settings("suffix", "_" + time_now_formatted)

            elif self.__suffix_template == "suffix_timestamp_custom":
                time_now = datetime.datetime.now()
                time_now_formatted = time_now.strftime("%Y%m%d_%H%M%S")
                suffix_custom_value = self.lineEdit_suffix_custom_value.text()
                self.update_parsing_settings(
                    "suffix", "_" + time_now_formatted + "_" + suffix_custom_value
                )

            elif self.__suffix_template == "suffix_timestamp_custom_empty":
                time_now = datetime.datetime.now()
                time_now_formatted = time_now.strftime("%Y%m%d_%H%M%S")
                self.update_parsing_settings("suffix", "_" + time_now_formatted)

            elif self.__suffix_template == "empty":
                self.update_parsing_settings("suffix", "")

            self.parsing_thread = ParsingThread(
                files_to_pars=self.__files_to_pars,
                target_directory=self.__target_directory,
                target_directory_changed=self.__target_directory_changed,
                parsing_settings=self.__parsing_settings,
            )
            self.parsing_thread.start()
            self.parsing_thread.signal.connect(self.parsing_thread_done)

            self.parsing_thread.progress.connect(self.conversion_progress)
            self.parsing_thread.file_conversion_ended.connect(
                self.file_conversion_ended
            )

        except Exception as e:
            color = "black"
            self.print_log("\nUps... ERROR occurred. \n\n" + str(e), color=color)
            traceback.print_exc()
            print(">>>", e, "<<<")

    def file_conversion_ended(self):
        """
        Function sends notification via status bar about ending of conversion for each input file.
        """
        self.__file_conversion_counter += 1
        info = (
            str(self.__file_conversion_counter)
            + " of "
            + str(len(self.__files_to_pars))
            + " converted"
        )
        self.statusbar.showMessage(info)
        self.statusbar.repaint()

    def conversion_progress(self, row_number, all_rows_number):
        """
        Function shows conversion progress for each input file.

        Input parameters are used to set progress bar values.

        :param row_number: number of currently processed row of input file currently processed
        :param all_rows_number: number of all rows of input file currently processed
        """
        self.progressBar.setRange(0, all_rows_number)
        self.progressBar.setValue(row_number)

    def parsing_thread_done(self, info):
        if "[action=start]" in info:
            color = "green"
            self.print_log(info, color)
        elif "[action=end]" in info:
            color = "green"
            self.print_log(info, color)
        else:
            color = "black"
            self.print_log(info, color)

    def update_parsing_settings(self, setting_name, setting_value):
        """
        Function gets current parsing settings and updates dictionary containing all parsing settings.
        :param setting_name: setting key name
        :param setting_value: setting value
        """
        self.__parsing_settings[setting_name] = setting_value

    def set_suffix(self, suffix_value):
        """
        Function sets given suffix into private variable __suffix and update parsing settings.
        :param suffix_value: input suffix
        """
        self.__suffix = suffix_value
        self.update_parsing_settings("suffix", suffix_value)

    def change_suffix(self, suffix_value_new):
        """
        Function changes given suffix in private variable.

        Confirmation is send to GUI into progress preview.
        :param suffix_value_new: new suffix value
        """
        old_suffix = self.__suffix
        new_suffix = suffix_value_new

        self.set_suffix(new_suffix)

        color = "green"
        info = 'Suffix changed from "' + old_suffix + '" to "' + self.__suffix + '"'
        self.print_log(info, color)

    def set_delimiter(self, delimiter_value):
        """
        Function sets given delimiter into private variable __delimiter and update parsing settings.

        :param delimiter_value: input delimiter
        """
        self.__delimiter = delimiter_value
        self.update_parsing_settings("csv_delimiter", delimiter_value)

    def get_delimiter(self):
        """
        Function gets delimiter from private variable and set it into lineEdit_separator.
        """
        self.lineEdit_separator.setText(self.__delimiter)

    def auto_detect_separator_changed(self):
        """
        Function handles auto-detect separator checkbox state change.
        """
        auto_detect_enabled = self.checkBox_auto_detect_separator.isChecked()
        self.update_parsing_settings("auto_detect_separator", auto_detect_enabled)

        # Disable/enable manual separator input based on checkbox state
        self.lineEdit_separator.setEnabled(not auto_detect_enabled)
        self.pushButton_separator_change.setEnabled(not auto_detect_enabled)

        if auto_detect_enabled:
            color = "green"
            info = "Auto-detect separator enabled. Separator will be detected for each file automatically."
            self.print_log(info, color)
        else:
            color = "black"
            info = (
                'Auto-detect separator disabled. Using manual separator: "'
                + self.__delimiter
                + '"'
            )
            self.print_log(info, color)

    def change_delimiter(self):
        """
        Function changes given delimiter in private variable.

        Confirmation is send to GUI into progress preview.
        """
        old_delimiter = self.__delimiter
        new_delimiter = self.lineEdit_separator.text()

        self.set_delimiter(new_delimiter)

        color = "green"
        info = (
            'Delimiter changed from "'
            + old_delimiter
            + '" to "'
            + self.__delimiter
            + '"'
        )
        self.print_log(info, color)

    def set_target_directory(self, target_directory_value):
        """
        Function sets given target directory into private variable __target_directory.

        :param target_directory_value: target directory
        """
        self.__target_directory = target_directory_value

    def get_target_directory_from_file(self):
        """
        Function gets target directory from private variable __target_directory
        and set it into lineEdit_target_directory.

        Only if user used selection by one or more files.
        """
        self.lineEdit_target_directory.setText(self.__target_directory)

    def get_target_directory_from_directory(self):
        """
        Function gets target directory from private variable __target_directory
        and set it into lineEdit_target_directory.

        Only if user used selection by directory. If subdirectories exist for given directory additional
        information is displayed in GUI.

        """
        number_of_subdirectories = self.check_if_subdirectory_exist(
            self.__target_directory
        )
        # print(number_of_subdirectories)
        if number_of_subdirectories:
            info = " (and subdirectories)"
        else:
            info = ""

        self.lineEdit_target_directory.setText(self.__target_directory + info)

    def change_target_directory(self):
        """
        Function changes target directory and set it in private variable __target_directory.

        Confirmation is send to GUI into progress preview.
        """
        old_target_directory = self.__target_directory

        title = "Choose new target directory"
        starting_directory = ""
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly

        file_dialog = QFileDialog()

        directories = file_dialog.getExistingDirectory(
            None, title, starting_directory, options=options
        )

        if directories:
            self.set_target_directory(directories)
            self.get_target_directory_from_file()

            color = "green"
            info = (
                'Target directory changed from "'
                + old_target_directory
                + '" to "'
                + self.__target_directory
                + '"'
            )
            self.print_log(info, color)
            self.__target_directory_changed = True
        else:
            info = "Target directory not changed."
            color = "black"
            self.print_log(info, color=color)

    def open_files(self):
        """
        Function get list of files via dialog window.

        Possible to select one or more files.
        """
        info = "File\\-s opening."
        color = "black"
        self.print_log(info, color=color)

        extension = "*.csv"

        title = "Open {0} files".format(extension)
        starting_directory = ""
        file_filter = "CSV ({0})".format(extension)
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        files = file_dialog.getOpenFileNames(
            self, title, starting_directory, filter=file_filter, options=options
        )
        files_only = files[0]
        # print(len(files_only),files_only)
        if len(files_only):
            # print(files)
            # print(files_only)

            for file in files_only:
                # print(file)
                target_directory2 = os.path.dirname(os.path.abspath(file))
                self.set_target_directory(target_directory2)
                # print(target_directory2)

            self.get_target_directory_from_file()
            self.list_of_files_to_pars(files_only)
            self.pushButton_start.setEnabled(True)
            self.__target_directory_changed = False
        else:
            number_of_files = 0
            info = "Selected {0} files.".format(str(number_of_files))
            color = "black"
            self.print_log(info, color=color)

    @staticmethod
    def check_if_subdirectory_exist(main_directory):
        """
        Function verifies whether provided directory has any subdirectories.

        :param main_directory: path to selected directory
        :return: 0 if there is no subdirectories
                 number > 0 if there is any directory, where number gives information about number of subdirectories.
        """
        pattern = os.path.join(main_directory, "*")
        number_of_directories = 0
        for candidate in glob.glob(pattern):
            if os.path.isdir(candidate):
                number_of_directories += 1
                break
        return number_of_directories

    def open_directory(self):
        """
        Function gets list of files via dialog window.

        Possible to get files from selected directory and subdirectories.
        """
        info = "Files from directory and subdirectories opening."
        color = "black"
        self.print_log(info, color=color)

        extension = "*.csv"

        title = "Open {0} files directory".format(extension)
        starting_directory = ""
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly

        file_dialog = QFileDialog()
        directories = file_dialog.getExistingDirectory(
            None, title, starting_directory, options=options
        )
        os_separator = os.path.sep

        if directories:
            self.set_target_directory(directories)
            self.get_target_directory_from_directory()

            files = glob.glob(
                directories + os_separator + "**" + os_separator + extension,
                recursive=True,
            )
            print(files)
            self.list_of_files_to_pars(files)
            self.pushButton_start.setEnabled(True)
            self.__target_directory_changed = False

        else:
            number_of_files = 0
            info = "Selected {0} files.".format(str(number_of_files))
            color = "black"
            self.print_log(info, color=color)

    def open_target_directory(self):
        """
        Function open target directory taking into account Operating system:
        Linux: Linux
        Mac: Darwin
        Windows: Windows
        """

        os_name = platform.system()
        if os_name == "Darwin":
            subprocess.call(["open", self.__target_directory])
        elif os_name == "Windows":
            subprocess.call(["explorer", self.__target_directory])
        elif os_name == "Linux":
            subprocess.call(["nautilus", self.__target_directory])
        else:
            info = "Can't open directory, your Operating System {0} is not supported. Please report it to us.".format(
                os_name
            )
            color = "red"
            self.print_log(info, color=color)

    def is_dark_mode(self):
        """
        Detects if the application is running in dark mode.
        """
        app_palette = QApplication.palette()
        bg_color = app_palette.color(QPalette.ColorRole.Window)

        return bg_color.lightness() < 128  # lightness < 128 means dark mode

    def print_log(self, log_value, color):
        """
        Function displays actions information in GUI in Progress preview.

        :param log_value: information to display
        :param color: color for given information
        """

        dark_mode = self.is_dark_mode()

        # Define colors for light and dark mode
        color_map = {
            "black": (0, 0, 0) if not dark_mode else (255, 255, 255),
            "red": (230, 30, 30) if not dark_mode else (255, 100, 100),
            "green": (60, 160, 60) if not dark_mode else (100, 255, 100),
            "blue": (0, 0, 255) if not dark_mode else (100, 180, 255),
            "orange": (255, 165, 0) if not dark_mode else (255, 200, 120),
            "default": (0, 0, 0) if not dark_mode else (255, 255, 255),
        }

        r, g, b = color_map.get(color, color_map["default"])

        log_output = (
            "["
            + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            + "] "
            + log_value
        )

        html_output = f"""<div style="color: rgb({r}, {g}, {b});">{log_output}</div>"""

        cursor = self.textBrowser_progress.textCursor()
        cursor.movePosition(QTextCursor.End)

        if not self.textBrowser_progress.document().isEmpty():
            cursor.insertBlock()

        block_fmt = cursor.blockFormat()
        block_fmt.setBottomMargin(4.0)
        cursor.setBlockFormat(block_fmt)

        frag = QTextDocumentFragment.fromHtml(html_output)
        cursor.insertFragment(frag)

        self.textBrowser_progress.setTextCursor(cursor)
        self.textBrowser_progress.repaint()

    def exit_application(self):
        """
        Function to exit from application.
        """
        info = "Exit application"
        print(info)
        color = "black"
        self.print_log(info, color=color)
        self.close()

    def list_of_files_to_pars(self, files):
        """
        Function sets private variables:
        __files_to_pars with list of selected files,
        __file_conversion_counter reset to 0

        :param files: list of selected files.
        """
        number_of_files = len(files)
        if number_of_files == 1:
            suffix = ""
        else:
            suffix = "s"
        info = "Selected {0} file{1}:".format(str(number_of_files), suffix)
        color = "black"
        self.print_log(info, color=color)
        self.__files_to_pars = files

        color = "black"
        for file in self.__files_to_pars:
            # self.print_log(file, color=color)
            action_name = "info "
            notification_info = "[action={0}] [source_file={1}]".format(
                action_name, file
            )
            self.print_log(notification_info, color=color)

        self.__file_conversion_counter = 0


class ParsingThread(QThread):
    signal = pyqtSignal("PyQt_PyObject")
    progress = pyqtSignal(int, int)
    file_conversion_ended = pyqtSignal(int)
    file_conversion_started = pyqtSignal(int)

    def __init__(
        self,
        files_to_pars,
        target_directory,
        target_directory_changed,
        parsing_settings,
        parent=None,
    ):
        super(ParsingThread, self).__init__(parent)

        self.files_to_pars = files_to_pars
        self.target_directory_changed = target_directory_changed
        self.target_directory = target_directory
        self.parsing_settings = parsing_settings

    def run(self):
        files_to_pars = self.files_to_pars
        target_directory_changed = self.target_directory_changed
        target_directory = self.target_directory
        source_file_delimiter = self.parsing_settings["csv_delimiter"]
        auto_detect_separator = self.parsing_settings.get(
            "auto_detect_separator", False
        )

        if "suffix" in self.parsing_settings:
            suffix = self.parsing_settings["suffix"]
            print("suffix: ", suffix)
        else:
            suffix = ""

        for source_file_name_with_path in files_to_pars:
            source_file_name = os.path.basename(source_file_name_with_path)
            source_file_name_without_extension = os.path.splitext(source_file_name)[0]
            source_file_extension = os.path.splitext(source_file_name)[1]
            source_file_path = os.path.dirname(
                os.path.abspath(source_file_name_with_path)
            )
            target_file_name = source_file_name_without_extension + suffix + ".xlsx"
            target_file_path = os.path.dirname(
                os.path.abspath(source_file_name_with_path)
            )

            if target_directory_changed:
                directory_to_save = target_directory
            else:
                directory_to_save = target_file_path

            final_path_to_save = directory_to_save + "/" + target_file_name

            start_time = time.time()

            self.log_emitter("start", source_file_name)
            self.file_conversion_started.emit(1)
            self.log_emitter(
                "info",
                source_file_name,
                "[source_file_path={0}]".format(source_file_path),
            )
            self.log_emitter(
                "info",
                source_file_name,
                "[source_file_extension={0}]".format(source_file_extension),
            )

            source_file_size = utilities.size_of_file_human(source_file_name_with_path)
            self.log_emitter(
                "info",
                source_file_name,
                "[source_file_size={0}]".format(source_file_size),
            )

            source_file_encoding = utilities.check_file_encoding(
                source_file_name_with_path
            )
            self.log_emitter(
                "info",
                source_file_name,
                "[source_file_encoding={0}]".format(source_file_encoding),
            )

            # Auto-detect separator if enabled
            if auto_detect_separator:
                detected_delimiter = utilities.detect_csv_separator(
                    source_file_name_with_path
                )
                # Format separator for display
                separator_display = detected_delimiter
                if detected_delimiter == "\t":
                    separator_display = "TAB"
                elif detected_delimiter == " ":
                    separator_display = "SPACE"
                elif not detected_delimiter.isprintable():
                    separator_display = repr(detected_delimiter)
                self.log_emitter(
                    "info",
                    source_file_name,
                    "[detected_separator={0}]".format(separator_display),
                )
                file_delimiter = detected_delimiter
            else:
                file_delimiter = source_file_delimiter

            source_file_lines_number = utilities.csv_file_row_counter(
                source_file_name_with_path, file_delimiter
            )
            self.log_emitter(
                "info",
                source_file_name,
                "[source_file_lines_number={0}]".format(str(source_file_lines_number)),
            )

            file = open(source_file_name_with_path, "r", encoding=source_file_encoding)
            csv.register_dialect("colons", delimiter=file_delimiter)
            reader = csv.reader(file, dialect="colons")

            workbook = xlsxwriter.Workbook(
                final_path_to_save, {"constant_memory": True}
            )
            worksheet = workbook.add_worksheet("details")

            for row_index, row in enumerate(reader):
                row_info = row_index + 1
                self.progress.emit(row_info, source_file_lines_number)
                # print(row_info, source_file_lines_number, source_file_name)
                for column_index, cell in enumerate(row):
                    # print(">",cell,"<")
                    worksheet.write(row_index, column_index, cell)

            self.log_emitter(
                "info",
                source_file_name,
                "[target_file_name={0}] [file saving]".format(target_file_name),
            )
            workbook.close()

            self.log_emitter(
                "end",
                source_file_name,
                "[target_file_name={0}] [file saved]".format(target_file_name),
            )

            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_time_parsed = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

            self.log_emitter(
                "info",
                source_file_name,
                "[elapsed_time={0}]".format(elapsed_time_parsed),
            )
            self.log_emitter(
                "info",
                source_file_name,
                "[target_file_path={0}]".format(directory_to_save),
            )
            self.file_conversion_ended.emit(1)

    def log_emitter(self, action_name, source_file_name, additional_info=""):
        """
        Function emits information from thread to display it in GUI.

        :param action_name: information about action name
        :param source_file_name: information about related source file
        :param additional_info: add more information if needed
        """
        notification = "[action={0}] [source_file_name={1}] {2}".format(
            action_name, source_file_name, additional_info
        )
        self.signal.emit(notification)


def main():
    if getattr(sys, "frozen", False):
        os.chdir(os.path.dirname(sys.executable))

    app = QApplication(sys.argv)
    form = MainWindow()

    app_name = __about__.__title__
    app_version = __about__.__version__
    app_version_release_date = __about__.__release_date__
    app.setApplicationName(app_name)
    app.setApplicationVersion(app_version)
    name = app.applicationName()
    version = app.applicationVersion()

    app_window_title = name
    form.setWindowTitle(app_window_title)

    # app_icon_file_name_png = 'LimberDuck-Converter-CSV.png'
    # app_icon_file_name_png_to_ico = utilities.png_to_ico(app_icon_file_name_png)
    # app_icon_file_name_ico_to_base64 = utilities.file_to_base64(app_icon_file_name_png_to_ico)
    # app_icon_file_name_ico = utilities.base64_to_ico(app_icon_file_name_ico_to_base64,app_icon_file_name_png)
    # app_icon_file_name_ico = 'LimberDuck-Converter-CSV.ico'

    icon_file_name = __about__.__icon__
    utilities.base64_to_ico(ldcc_ico.ico, icon_file_name)

    app.setWindowIcon(QIcon(icon_file_name))

    os.remove(icon_file_name)

    form.show()
    QTimer.singleShot(5, form.display_update_window)
    sys.exit(app.exec_())
