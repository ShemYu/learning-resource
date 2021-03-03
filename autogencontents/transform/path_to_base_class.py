# -*- coding: utf-8 -*-
__author__ = "Shem_Yu"

from autogencontents.base.base_class import Path
import os


class ReadingLoader():
    """from path to Sections and MarkdownReading"""
    def __init__(self, dirs:str = None, reading_type:list = [".md"]):
        """Init.

        Args:
            dirs (str, optional): root to walk. Defaults to None.
            reading_type (list, optional): List of what to find. Defaults to [".md"].
        """        
        self.path = dirs if dirs else os.path.join(os.getcwd(), "reading")
    def _walk_and_parse(self):
        """Walk path method."""
        print("Walk through {}".format(self.path))
        path_list = []
        for walk_result in os.walk(self.path):
            path_list.append(Path(walk_result))
        
        self._parse(path_list)
        return path_list
    
    def _parse(self, path_list):
        for path in path_list:
            print(path.files)
        
    def get_structure(self):
        raw_paths = self._walk_and_parse()
        
