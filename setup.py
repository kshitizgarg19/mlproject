from setuptools import find_packages
from typing import List
from setuptools import setup
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        
setup(
    name='mlproject',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    author='kshitiz',
    author_email='kshitizgarg19@gmail.com',install_requires=get_requirements('requirements.txt')
)