# -*- coding: utf-8 -*-
__author__ = "Shem_Yu"

import os



class ReadingLoader:
    """from path to Sections and MarkdownReading"""

    def __init__(self, dirs: str = None, reading_type: list = [".md"]):
        """Init.

        Args:
            dirs (str, optional): root to walk. Defaults to None.
            reading_type (list, optional): List of what to find. Defaults to [".md"].
        """
        self.path = dirs if dirs else os.path.join(os.getcwd(), "reading")

    def _walk_and_parse(self):
        """Walk path method."""
        from autogencontents.base.base_class import Path
        print("Walk through {}".format(self.path))
        Contents = ""
        for walk_result in os.walk(self.path):
            p = Path(walk_result)
            Contents += str(p.sec) + "\n"
            Contents += "\n".join([str(r) for r in p.files])
            Contents += "\n"
        return Contents
    
    def get_structure(self):
        return self._walk_and_parse()
