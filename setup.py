from importlib.resources import Package
from setuptools import setup, find_packages
from typing import List

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines().remove("-e .")


#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="Srihari"
DESRCIPTION="This is the first end-to-end Machine Learning Project"
PACKAGES =find_packages()
REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=PACKAGES, 
install_requires=get_requirements_list()
)
