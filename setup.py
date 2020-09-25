# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in dignity_survey/__init__.py
from dignity_survey import __version__ as version

setup(
	name='dignity_survey',
	version=version,
	description='Survey records',
	author='OpeneTechnologies',
	author_email='hello@openetech.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
