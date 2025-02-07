"""
The setup.py file is an essential part of the packaging and distributing
Python projects. It is used by setuptools (or distutils in older Python versions)
to define the configuration of your project, such as metadata, dependencies, etc.
"""

from setuptools import setup,find_packages
from typing import List

# List of dependencies
def get_requirements()->List[str]:
    """
    This function will return a list of requirements needed to build
    and install the project.
    """
    requirement_list : List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            # read lines from the file
            lines = file.readlines()
            for line in lines:

                # remove leading and trailing whitespaces
                requirement = line.strip()

                # skip empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_list

#print(get_requirements())

setup(
    name='SentinelX',
    version='0.0.1',
    description='A Python package for phishing URL detection using Machine Learning. Built with setuptools for easy installation and deployment. Includes feature extraction, dataset preprocessing, model training, and evaluation.',
    author='Stephen Acheampong',
    author_email='acheampongstephen392024@gmail.com',
    url='https://github.com/AcheampongStephen/SentinelX',
    packages=find_packages(),
    install_requires=get_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords=['phishing', 'url detection', 'ML'],
    project_urls={
        'Documentation': 'https://github.com/AcheampongStephen/SentinelX/blob/master/README.md',
        'Source Code': 'https://github.com/AcheampongStephen/SentinelX',
        'Issue Tracker': 'https://github.com/AcheampongStephen/SentinelX/issues',
    },
    python_requires='>=3.10'
)