# setup.py
from setuptools import setup, find_packages

requires = [
    "python-dotenv",
    "pymongo==3.10.1",
    "Flask-PyMongo==2.3.0"
]

setup(
    name='esgauth',
    version='0.1',
    packages=find_packages(),
    install_requires=requires,
)
