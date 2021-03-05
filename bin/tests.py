"""Testing module."""
import sys, os

sys.path.append(os.getcwd())

from autogencontents.base import Readme

if __name__ == "__main__":
    Readme().auto_generate_contents()