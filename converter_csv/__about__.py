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

__all__ = [
    "__title__",
    "__icon__",
    "__summary__",
    "__uri__",
    "__version__",
    "__release_date__",
    "__author__",
    "__email__",
    "__license_name__",
    "__license_link__",
    "__copyright__",
]

__title__ = "Converter CSV by LimberDuck"
__package_name__ = "converter-csv"
__icon__ = "LimberDuck-converter-csv.ico"
__summary__ = "Converter CSV by LimberDuck is a GUI tool to convert multiple large csv files to xlsx files."
__uri__ = "https://limberduck.org"
__version__ = "0.4.0"
__release_date__ = "2025.09.01"
__author__ = "Damian Krawczyk"
__email__ = "damian.krawczyk@limberduck.org"
__license_name__ = "GNU GPLv3"
__license_link__ = "https://www.gnu.org/licenses/gpl-3.0.en.html"
__copyright__ = "\N{COPYRIGHT SIGN} 2018-{} by {}".format(
    datetime.datetime.now().year, __author__
)
