import sys, os

from autogencontents.transform import ReadingLoade


def generate(root_dir='reading'):
    rl = ReadingLoader()
    rl.get_structure()


if __name__ == "__main__":
    generate()