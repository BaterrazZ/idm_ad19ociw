from distutils.core import setup
from setuptools import find_packages

setup(name='ad19ociw',
      version='0.1',
      author='Paul Zech',
      author_email='paul.zech@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets'])
