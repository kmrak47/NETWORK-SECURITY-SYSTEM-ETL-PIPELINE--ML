''' 
The setup.py file is an essential part of packaging and distributing python projects. 
It is used by setup tools (or distutils in older python versions) to define 
the configuration of project, such as metadata, dependencies and more. / basic info on versions.
'''

from setuptools import find_packages,setup #it will find all the packages in folder
from typing import List

def get_requirements()-> list[str]:
    """
    this function returns list of requirements
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines = file.readlines()
            ## process each line
            for line in lines:
                requirement = line.strip()
                ##ignore empty lines and .e  in req.txt file
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")


    return requirement_lst


print(get_requirements())


setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = 'Ankit kumar',
    author_email = "kmrak789704@gmail.com",
    packages = find_packages(),
    install_requires= get_requirements()
)

#-e . refers to setup.py file







