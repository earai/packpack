from distutils.core import setup

setup(
name='packpack',
version='0.0.1',
packages=['packpack'],
description='A backpack packing inference application.',
author='erai',
url='https://github.com/earai/packpack',
install_requires=open('requirements.txt').read().splitlines()
)