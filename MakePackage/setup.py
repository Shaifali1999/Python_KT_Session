# https://pypi.org/project/setuptools/
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0',
    description='The demo package',
    author='Muthukumar Subramanian',
    license='MIT',
    author_email='muthukumar@example.com',
    packages=find_packages('.'),
    package_dir={'': '.'}
)
