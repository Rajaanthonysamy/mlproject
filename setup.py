from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT="-e ."

def get_requirements(filename:str)->List[str]:
    requirements=[]
    with open(filename) as f:
        requirements = [req.replace("\n", "") for req in f.readlines()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.1',
    author='RajaAnthonysamy',
    packages=find_packages(),
    author_email="rajaanthonysamy5798@gmail.com",
insstall_requires=get_requirements("requirements.txt"),)