import os

import setuptools
from setuptools import setup
from setuptools import version


_HERE = os.path.dirname(__file__)

version_file = "autogencontents/version.py"


if __name__ == "__main__":
    setup(
        name = "autogencontents",
        version = "0.1",
        Descriptions = "Automatically generate contents of reading.",
        author = "Shem Yu",
        license = "PSF",
        packages = setuptools.find_packages(exclude=[
            "bin.*",
            "reading.*"
        ])
    )