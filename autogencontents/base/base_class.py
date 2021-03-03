"""Define base class."""
# -*- coding: utf-8 -*-
__author__ = "Shem_Yu"


import os


class Path():
    """Path object return by os.walk"""
    def __init__(self, walk_result):
        self.arg = walk_result[0]
        self.dirnames = walk_result[1]
        self.files = walk_result[2]
class Section():
    """Sections in contents."""
    def __init__(self, path, depth=0):
        self.depth = depth


class Reading(Path):
    """Reading in contents"""
    def __init__(self, sec:Section, name):
        self.section = sec
        self.name = name
    def __str__(self) -> str:
        str_type = "{}- {}".format("\t"*self.section.depth, self.name)
        return str_type
    def __repr__(self) -> str:
        return self.__str__()
    