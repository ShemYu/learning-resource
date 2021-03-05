# -*- coding: utf-8 -*-
"""Define base class."""
__author__ = "Shem_Yu"

import os
import urllib.parse as parse

_OWNER_NAME = "ShemYu"
_REPO_NAME = "learning-resource"

if os.name == "nt":
    _DIR_SEP_TAG = "\\"
else:
    _DIR_SEP_TAG = "/"


class Path:
    """Path object return by os.walk"""

    def __init__(self, walk_result, dirs: str = ""):
        self.root = dirs if dirs else os.path.join(os.getcwd())
        self.arg = walk_result[0].replace(self.root, "")
        self.sec = Section(self.arg)
        self.dirs = walk_result[1]
        self.files = [Reading(self.sec, r) for r in walk_result[2]]

    def __str__(self) -> str:
        repr_str = "now: {}\ndirs here: {}\nfiles here: {}\n============".format(
            self.arg, self.dirs, self.files
        )
        return repr_str


class Section:
    """Sections in contents."""

    def __init__(self, path):
        self.dirname_list = path.split(_DIR_SEP_TAG)
        self.depth = len(self.dirname_list) - 1
        self.name = self.dirname_list[-1]

    def __str__(self) -> str:
        _str = "{}- {}".format("\t" * self.depth, self.name)
        return _str


class Reading:
    """Reading in contents"""

    def __init__(self, sec: Section, name):
        self.section = sec
        self.name = name
        # https://github.com/{OWNER_NAME}/{REPO_NAME}/blob/master/{PATH_TO_READING}/{READING_NAME}
        self.url = "https://github.com/{}/{}/blob/read/{}/{}".format(
            _OWNER_NAME,
            _REPO_NAME,
            parse.quote("/".join(self.section.dirname_list)),
            parse.quote(self.name),
        )

    def __str__(self) -> str:
        str_type = "{}1. [{}]({})".format(
            "\t" * (self.section.depth + 1), self.name, self.url
        )
        return str_type

    def __repr__(self) -> str:
        return self.name


class Readme:
    def __init__(self, file_path:str="README.md"):
        self.file_path = file_path
        self._load()

    def _load(self, reload_path:str=""):
        self.file_path = reload_path if reload_path else self.file_path
        rdmd = open(self.file_path, 'r', encoding="utf8")
        self._content = rdmd.read()

    def _save(self):
        rdmd = open(self.file_path,'w', encoding="utf8")
        rdmd.write(self.content)

    def __str__(self) -> str:
        return str(self.content)
        
    def __repr__(self) -> str:
        return str(self.content)

    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        self._content = value
    
    @property
    def abstract(self):
        self._abstract = self.content.split("# Contents\n\n")[0]
        return self._abstract
    
    @abstract.setter
    def abstract(self, new_abstract:str = ""):
        self._abstract = new_abstract
        self.content = "{}\n# Contents\n\n{}".format(self._abstract, self.contents)
    
    @property
    def contents(self):
        self._contents = self.content.split("# Contents\n\n")[1]
        return self._contents
    
    @contents.setter
    def contents(self, new_contents):
        self._contents = new_contents
        self.content = "{}# Contents\n\n{}".format(self.abstract, self._contents)
    
    def auto_generate_contents(self, root_path="reading"):
        from autogencontents.transform.path_to_contents import ReadingLoader
        rl = ReadingLoader(dirs=root_path)
        new_contents = rl.get_structure()
        self.contents = new_contents
        self._save()
