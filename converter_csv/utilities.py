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

import base64
# import imageio
import os
import chardet
import csv
import requests
from datetime import datetime
from typing import List, Dict
import re
from packaging import version
from converter_csv import __about__


def file_to_base64(filename):
    """
    Function converts given file into base64.

    :param filename: input file name with path
    :return: base64 string
    """
    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string


# def png_to_ico(filename):
#     """
#     Function converts given png file into ico.

#     :param filename: png file name
#     :return: ico file name
#     """
#     filename_without_extension = os.path.splitext(filename)[0]
#     target_file_name = filename_without_extension + ".ico"
#     img = imageio.imread(filename)
#     imageio.imwrite(target_file_name, img)

#     # img = Image.open(filename)
#     # icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
#     # img.save(target_file_name, sizes=icon_sizes)

#     return target_file_name


def base64_to_ico(ico_in_base64, filename):
    """
    Function write base64 string as ico file with pointed filename

    :param ico_in_base64:
    :param filename: get filename with extension to use it as target file name
    :return: ico file name
    """
    filename_without_extension = os.path.splitext(filename)[0]
    target_file_name = filename_without_extension + ".ico"
    icondata = base64.b64decode(ico_in_base64)
    iconfile = open(target_file_name, "wb")
    iconfile.write(icondata)
    iconfile.close()

    return target_file_name


def check_file_encoding(file):
    """
    Function checks encoding for input file.

    :param file: input file path
    :return: file encoding eg. 'ascii', 'utf8'
    """
    raw_data = open(file, "rb").read()
    result = chardet.detect(raw_data)
    char_enc = result["encoding"]

    return char_enc


def size_of_file_human(file, suffix="B"):
    """
    Function convert provided file size into human readable form
    :param file:  source file name with path
    :param suffix: suffix
    :return: file size in human readable form
    """
    num = os.path.getsize(file)

    for unit in [" b", " Ki", " Mi", " Gi", " Ti", " Pi", " Ei", " Zi"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)


def detect_csv_separator(file, num_lines=5):
    """
    Function detects CSV separator by analyzing the first few lines of the file.

    :param file: input file path
    :param num_lines: number of lines to analyze (default: 5)
    :return: detected separator character (e.g., ',', ';', '\t', '|')
    """
    source_file_encoding = check_file_encoding(file)

    # Common CSV separators to try
    separators = [",", ";", "\t", "|", ":"]

    try:
        with open(file, "r", encoding=source_file_encoding) as f:
            # Read first few lines
            lines = []
            sample = ""
            for i, line in enumerate(f):
                if i >= num_lines:
                    break
                lines.append(line.rstrip("\n\r"))
                sample += line
                if len(sample) > 1024:
                    break

            if not lines:
                # If file is empty, default to comma
                return ","

            # Count columns for each separator
            separator_scores = {}
            for sep in separators:
                column_counts = []
                for line in lines:
                    if line.strip():  # Skip empty lines
                        # Count occurrences of separator
                        count = line.count(sep)
                        column_counts.append(count)

                if column_counts:
                    # Score based on consistency: prefer separators that produce
                    # consistent column counts across lines
                    if len(set(column_counts)) == 1 and column_counts[0] > 0:
                        # All lines have the same number of columns (perfect match)
                        separator_scores[sep] = column_counts[0] * 1000 + len(
                            column_counts
                        )
                    elif column_counts:
                        # Calculate variance - lower is better
                        avg = sum(column_counts) / len(column_counts)
                        variance = sum((x - avg) ** 2 for x in column_counts) / len(
                            column_counts
                        )
                        # Higher score for more columns and lower variance
                        separator_scores[sep] = avg * 100 - variance

            if separator_scores:
                # Return separator with highest score
                detected_sep = max(separator_scores, key=separator_scores.get)
                return detected_sep

            # Fallback: try csv.Sniffer
            sniffer = csv.Sniffer()
            try:
                # csv.Sniffer expects delimiters as a string of characters
                delimiter_string = "".join(separators)
                dialect = sniffer.sniff(sample, delimiters=delimiter_string)
                return dialect.delimiter
            except:
                pass

    except Exception as e:
        # If detection fails, default to comma
        return ","

    # Default fallback
    return ","


def csv_file_row_counter(file, source_file_delimiter):
    """
    Function counts number of rows for selected input file.

    :param file: input file path
    :param source_file_delimiter: values delimiter
    :return: number of rows
    """
    source_file_encoding = check_file_encoding(file)
    file = open(file, "r", encoding=source_file_encoding)
    csv.register_dialect("colons", delimiter=source_file_delimiter)
    reader = csv.reader(file, dialect="colons")

    row_count = sum(1 for row in reader)
    return row_count


def get_announcements(tool: str, current_version: str) -> List[Dict[str, str]]:
    """
    Fetches announcements from LimberDuck GitHub Pages and returns a list of
    dicts with "type", "title", and "message" for entries matching the tool,
    valid date range, and version condition.

    Args:
        tool (str): Tool name to filter announcements by (e.g., "converter-csv").
        current_version (str): Current version of the tool (e.g., "0.4.3").

    Returns:
        List[Dict[str, str]]: List of matching announcements.
    """

    url = "https://limberduck.github.io/data/announcements.json"
    today = datetime.now().date()
    results = []

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        # If no Internet or resource not reachable, return information
        info = "Could not fetch announcements. Please check your Internet connection."
        return [{"type": "info", "title": "Announcements", "message": info}]

    announcements = data.get("announcements", [])
    for item in announcements:
        try:
            valid_from = datetime.strptime(
                item.get("valid_from", "1900-01-01"), "%Y-%m-%d"
            ).date()
            valid_until = datetime.strptime(
                item.get("valid_until", "9999-12-31"), "%Y-%m-%d"
            ).date()

            if not (valid_from <= today <= valid_until):
                continue

            for t in item.get("tools", []):
                if t.get("name") == tool:
                    max_ver = t.get("max_version", "999.0.0")
                    if version.parse(current_version) <= version.parse(max_ver):

                        message = item.get("message", "")
                        url_pattern = r"(https?://[^\s]+)"
                        html_message = re.sub(
                            url_pattern, r'<a href="\1">\1</a>', message
                        )

                        results.append(
                            {
                                "type": item.get("type", "info"),
                                "title": item.get("title", ""),
                                "message": html_message,
                            }
                        )
                    break

        except Exception:
            continue

    return results
