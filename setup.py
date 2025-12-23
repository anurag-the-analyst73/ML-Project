from setuptools import find_packages,setup
from typing import List

_hyphen_e_dot = "-e."
def get_requirements(_fp:str)->List[str]:
    '''
    This function will return the list of requirements.txt
    '''
    _req = []
    with open(_fp) as file_obj:
        _req = file_obj.readlines()
        _req = [_r.replace("\n","") for _r in _req ]

        if _hyphen_e_dot in _req:
            _req.remove(_hyphen_e_dot)
    return _req


setup(
name='ML Project',
version='0.0.1',
author='Anurag Sarkar',
author_email='anurags12711@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')    
)