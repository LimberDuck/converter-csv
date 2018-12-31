# -*- coding: utf-8 -*-
u"""
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

from converter_csv import utilities

png_filename = '../icons/LimberDuck-converter-csv.png'

print(utilities.file_to_base64(utilities.png_to_ico(png_filename)))