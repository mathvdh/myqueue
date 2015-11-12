from setuptools import setup

setup(name='myqueue',
	version='0.2',
	description='My Queue',
	url='http://github.com/mathvdh/myqueue',
	author='Mathieu Van der Haegen',
	author_email='m@dcy.io',
	license='GPL',
	packages=['myqueue'],
	test_suite='nose2.collector.collector',
	tests_require=['nose2'],
	zip_safe=False)