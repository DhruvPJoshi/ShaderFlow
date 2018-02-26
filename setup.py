import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ShaderFlow",
    version = "0.0.1",
    author = "Dhruv Joshi",
    author_email = "dhruvjoshi997@gmail.com",
    description = ("A node-based shader editor.")
    long_description = read("README.md")
)