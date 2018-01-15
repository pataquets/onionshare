# -*- coding: utf-8 -*-
"""
OnionShare | https://onionshare.org/

Copyright (C) 2017 Micah Lee <micah@micahflee.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import json
import locale
import os

strings = {}


def load_strings(common, default="en"):
    """
    Loads translated strings and fallback to English
    if the translation does not exist.
    """
    global strings

    # find locale dir
    locale_dir = common.get_resource_path('locale')

    # load all translations
    translations = {}
    for filename in os.listdir(locale_dir):
        abs_filename = os.path.join(locale_dir, filename)
        lang, ext = os.path.splitext(filename)
        if ext == '.json':
            with open(abs_filename, encoding='utf-8') as f:
                translations[lang] = json.load(f)

    strings = translations[default]
    lc, enc = locale.getdefaultlocale()
    if lc:
        lang = lc[:2]
        if lang in translations:
            # if a string doesn't exist, fallback to English
            for key in translations[default]:
                if key in translations[lang]:
                    strings[key] = translations[lang][key]


def translated(k, gui=False):
    """
    Returns a translated string.
    """
    return strings[k]

_ = translated
