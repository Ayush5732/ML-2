from setuptools import find_packages,setup

from typing import List

temp = "-e ."

def import_requirements(file_path:str)-> List[str]:
    """
    Return a list of all libraries need to import 
    """
    libraries = []
    with open(file_path) as file_obj:
        libraries = file_obj.readlines()
        libraries = [req.replace("\n","") for req in libraries]
        if temp in libraries:
            libraries.remove(temp)
    return libraries 




setup(
    name= 'ML PROJECT NEW',
    version='0.0.1',
    author='Ayush',
    author_email='ayush97choudhary@gmail.com',
    packages=find_packages(),
    install_requires = import_requirements('requirements.txt')

)
