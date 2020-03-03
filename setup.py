from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf8') as f:
	long_description = f.read()

with open('requirements.txt') as f:
	requirements = f.read().splitlines()

setup(
	name='Fxnium',
	version='1.1.11',
	author='Liav Mordouch',
	author_email='liavmordouch@gmail.com',
	description='Fxnium is a python module for easy interactaction with the site fxp.co.il',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/Deftera186/Fxnium',
	packages=find_packages(),
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
            ],
	install_requires=requirements
)
