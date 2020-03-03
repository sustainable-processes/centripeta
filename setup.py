import os
import sys
import pkg_resources
from setuptools import setup
import pathlib
import shutil

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.md')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='centripeta',
    version='1.0.0',
    description="A robot for chemistry!",
    python_requires='==3.*,>=3.6.0',
    author='Kobi Felton',
    author_email='kcmf2@cam.ac.uk',
    packages=['centripeta'],
    install_requires=['pandas>=0.24.2', 'opencv-contrib-python>4.1', 'matplotlib>3.0', 
                      'picosdk @ https://api.github.com/repos/sustainable-processes/picosdk-python-wrappers/tarball/8c67fe67e58dcc4d6c2184b2f733ca3e40d14252',
                      'commanduino @ https://api.github.com/repos/marcosfelt/commanduino/tarball/f5718c27fe451c4eefe006cb38320f4e463788a1',
                      'pycont @ https://api.github.com/repos/croningp/pycont/tarball/815e25e4fb0c384f0acda5bc2346191292a3682'], 
)
