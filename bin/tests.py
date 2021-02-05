"""Testing module."""
import sys, os

sys.path.append(os.getcwd())

from autogencontents.transform import ReadingLoader


def generate(root_dir='reading'):
    """Get structure of specific reading with dict."""
    rl = ReadingLoader()
    rl.get_structure()


if __name__ == "__main__":
    generate()