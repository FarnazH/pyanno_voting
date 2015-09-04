import os
from setuptools import find_packages, setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyanno",
    version = "0.1a",
    author = "Farnaz",
    author_email = "farnazh@gmail.com",
    description = "PyAnno annotating things and labeling things and sorting things ",
    license = "BSD",
    keywords = "",
    url = "https://github.com/FarnazH/pyanno_voting.git",
    packages=find_packages(),
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
