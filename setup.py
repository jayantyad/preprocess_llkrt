import setuptools 

with open('readme.md','r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_llkrt', #this should be unique
	version = '0.0.1' ,
	author = 'Jayant Yadav',
	author_email = 'jayantyad@gmail.com',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = 'setuptools.find_packages()',
	classifiers = [
		'Programming Language :: Python ::3',
		'License :: OSI Approved :: MIT',
		'Operating System :: OS Independent'
		],
	python_requires = '>= 3.5'
	)