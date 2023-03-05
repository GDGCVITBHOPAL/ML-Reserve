from setuptools import setup,find_packages
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


#Declaring variables for setup functions
PROJECT_NAME="Customer-Personality-Analysis"
VERSION="0.0.1"
AUTHOR="vaasu2002"
DESRCIPTION="This is a small package of Customer-Personality-Analysis"
AUTHOR_EMAIL = "vaasu.bisht2021@vitbhopal.ac.in"
REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
author_email=AUTHOR_EMAIL,
long_description=long_description,
long_description_content="text/markdown",
description=DESRCIPTION,
packages=find_packages(), 
install_requires=get_requirements_list()
)