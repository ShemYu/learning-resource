# -*- coding: utf-8 -*-
__author__ = "Shem_Yu"

import os


class ReadingLoader():
    """from path to Sections and MarkdownReading"""
    def __init__(self, dirs:str = os.path.join("..", "reading"), reading_type:list = [".md"]):
        self.path = dirs
    def _walk(self):
        """Walk path method."""
        print(os.walk(self.path))
    def get_structure(self):
        self._walk()
