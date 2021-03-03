# -*- coding: utf-8 -*-
"""Define base class."""
__author__ = "Shem_Yu"


import os

_REPO_NAME = "learning-resource"

if os.name == "nt":
    _DIR_SEP_TAG = "\\"
else:
    _DIR_SEP_TAG = "/"


class Path:
    """Path object return by os.walk"""

    def __init__(self, walk_result, dirs: str = ""):
        self.root = dirs if dirs else os.path.join(os.getcwd(), "reading")
        self.arg = walk_result[0].replace(self.root, "")
        sec = Section(self.arg)
        self.dirs = walk_result[1]
        self.files = [Reading(sec, r) for r in walk_result[2]]

    def __str__(self) -> str:
        repr_str = "now: {}\ndirs here: {}\nfiles here: {}\n============".format(
            self.arg, self.dirs, self.files
        )
        return repr_str


class Section:
    """Sections in contents."""

    def __init__(self, path):
        dirname_list = path.split(_DIR_SEP_TAG)
        dep = len(dirname_list)
        self.depth = dep if dep > 0 else 1
        self.name = dirname_list[-1]

    def __str__(self) -> str:
        _str = "{}- {}".format("\t" * self.depth, self.name)
        return _str


class Reading:
    """Reading in contents"""

    def __init__(self, sec: Section, name):
        self.section = sec
        self.name = name

    def __str__(self) -> str:
        str_type = "{}- {}".format("\t" * (self.section.depth + 1), self.name)
        return str_type

    def __repr__(self) -> str:
        return self.name
