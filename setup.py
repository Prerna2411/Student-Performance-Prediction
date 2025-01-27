from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    '''this function will return list of requiremnts'''
    
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    return requirements

        if HYPEN_E_DOT IN REQ:
            requirements.remove(req)

setup(
name='mlproject',
version='0.0.1',
author='prerna',
author_email='pprerna42@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)

