from setuptools import setup
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python-syntaxdb",
    version = "0.0.1",
    author = "Rahul Arulkumaran",
    author_email = "rahulkumaran@gmail.com",
    description = ("A Python moudle for accessing the SyntaxDB API"),
    license = "MIT",
    keywords = "syntaxdb",
    url = "https://github.com/rahulkumaran/python-syntaxdb",
    packages=['syntaxdb'],
    long_description=read('README.rst'),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
    install_requires=[
        "requests",
    ],
    package_data={
        "": ["README.md", "LICENSE.md"]
    }
)
