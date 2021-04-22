from __future__ import absolute_import
import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='py3swf',
    version='1.5.5',
    description='SWF Parsing Utilities',
    long_description=read('README.md'),
    keywords="swf parser parsing decompile utilities",

    author='Tim Knip, Converted by: Swar Patel',
    author_email='tim@floorplanner.com',
    url='https://github.com/swar/py3swf',

    install_requires=["lxml>=3.3.0", "Pillow>=2.3.0", "pylzma>=0.4.6", "six"],
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
