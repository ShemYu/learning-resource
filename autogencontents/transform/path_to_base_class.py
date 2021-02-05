# -*- coding: utf-8 -*-
__author__ = "Shem_Yu"

import os


class ReadingLoader():
    """from path to Sections and MarkdownReading"""
    def __init__(self, dirs:str = None, reading_type:list = [".md"]):
        self.path = dirs if dirs else os.path.join(os.getcwd(), "reading")
    def _walk_and_parse(self):
        """Walk path method."""
        print("Walk through {}".format(self.path))
        return [i for i in os.walk(self.path)]
    
    def _parse(self, arg, dirnames, names):
        print(names)
        
    def get_structure(self):
        raw_paths = self._walk()
        self._parse(raw_paths)
        
