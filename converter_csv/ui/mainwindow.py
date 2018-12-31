# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 200))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_action = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_action.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_action.setMaximumSize(QtCore.QSize(16777215, 160))
        self.groupBox_action.setTitle("")
        self.groupBox_action.setObjectName("groupBox_action")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_action)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_action)
        self.pushButton_start.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_start.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_start.setToolTipDuration(-1)
        self.pushButton_start.setStatusTip("")
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_2.addWidget(self.pushButton_start)
        self.label_separator = QtWidgets.QLabel(self.groupBox_action)
        self.label_separator.setMinimumSize(QtCore.QSize(100, 0))
        self.label_separator.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_separator.setObjectName("label_separator")
        self.horizontalLayout_2.addWidget(self.label_separator)
        self.lineEdit_separator = QtWidgets.QLineEdit(self.groupBox_action)
        self.lineEdit_separator.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEdit_separator.setObjectName("lineEdit_separator")
        self.horizontalLayout_2.addWidget(self.lineEdit_separator)
        self.pushButton_separator_change = QtWidgets.QPushButton(self.groupBox_action)
        self.pushButton_separator_change.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_separator_change.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_separator_change.setObjectName("pushButton_separator_change")
        self.horizontalLayout_2.addWidget(self.pushButton_separator_change)
        self.label_target_directory = QtWidgets.QLabel(self.groupBox_action)
        self.label_target_directory.setObjectName("label_target_directory")
        self.horizontalLayout_2.addWidget(self.label_target_directory)
        self.lineEdit_target_directory = QtWidgets.QLineEdit(self.groupBox_action)
        self.lineEdit_target_directory.setReadOnly(True)
        self.lineEdit_target_directory.setObjectName("lineEdit_target_directory")
        self.horizontalLayout_2.addWidget(self.lineEdit_target_directory)
        self.pushButton_target_dir_change = QtWidgets.QPushButton(self.groupBox_action)
        self.pushButton_target_dir_change.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_target_dir_change.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_target_dir_change.setObjectName("pushButton_target_dir_change")
        self.horizontalLayout_2.addWidget(self.pushButton_target_dir_change)
        self.pushButton_target_dir_open = QtWidgets.QPushButton(self.groupBox_action)
        self.pushButton_target_dir_open.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_target_dir_open.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_target_dir_open.setObjectName("pushButton_target_dir_open")
        self.horizontalLayout_2.addWidget(self.pushButton_target_dir_open)
        self.verticalLayout.addWidget(self.groupBox_action)
        self.groupBox_progress = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_progress.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_progress.setObjectName("groupBox_progress")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_progress)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_progress = QtWidgets.QTextEdit(self.groupBox_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_progress.sizePolicy().hasHeightForWidth())
        self.textEdit_progress.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.textEdit_progress.setFont(font)
        self.textEdit_progress.setReadOnly(True)
        self.textEdit_progress.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_progress.setObjectName("textEdit_progress")
        self.horizontalLayout.addWidget(self.textEdit_progress)
        self.verticalLayout.addWidget(self.groupBox_progress)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAction = QtWidgets.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_directory.setObjectName("actionOpen_directory")
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionStart_conversion = QtWidgets.QAction(MainWindow)
        self.actionStart_conversion.setObjectName("actionStart_conversion")
        self.actionChange_separator = QtWidgets.QAction(MainWindow)
        self.actionChange_separator.setObjectName("actionChange_separator")
        self.actionChange_target_directory = QtWidgets.QAction(MainWindow)
        self.actionChange_target_directory.setObjectName("actionChange_target_directory")
        self.actionOpen_target_directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_target_directory.setObjectName("actionOpen_target_directory")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionOpen_directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAction.addAction(self.actionStart_conversion)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.actionChange_separator)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.actionChange_target_directory)
        self.menuAction.addAction(self.actionOpen_target_directory)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_start.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to <span style=\" font-weight:600;\">start </span>conversion of selected *.csv files.</p></body></html>"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.label_separator.setText(_translate("MainWindow", "Separator:"))
        self.lineEdit_separator.setToolTip(_translate("MainWindow", "<html><head/><body><p>Key-in separation sign e.g. ; or ,</p></body></html>"))
        self.pushButton_separator_change.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to <span style=\" font-weight:600;\">change separation sign</span>.</p></body></html>"))
        self.pushButton_separator_change.setText(_translate("MainWindow", "Change"))
        self.label_target_directory.setText(_translate("MainWindow", "Target directory:"))
        self.pushButton_target_dir_change.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to <span style=\" font-weight:600;\">change target directory</span> for output files.</p></body></html>"))
        self.pushButton_target_dir_change.setText(_translate("MainWindow", "Change"))
        self.pushButton_target_dir_open.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to <span style=\" font-weight:600;\">open target tiregtory</span>.</p></body></html>"))
        self.pushButton_target_dir_open.setText(_translate("MainWindow", "Open"))
        self.groupBox_progress.setTitle(_translate("MainWindow", "Progress preview"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAction.setTitle(_translate("MainWindow", "Action"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_directory.setText(_translate("MainWindow", "Open directory"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file\\-s"))
        self.actionStart_conversion.setText(_translate("MainWindow", "Start conversion"))
        self.actionChange_separator.setText(_translate("MainWindow", "Change separator"))
        self.actionChange_target_directory.setText(_translate("MainWindow", "Change target directory"))
        self.actionOpen_target_directory.setText(_translate("MainWindow", "Open target directory"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

