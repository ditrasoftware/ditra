from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ditra/__init__.py
from ditra import __version__ as version

setup(
	name="ditra",
	version=version,
	description="Digital Transformation Platform",
	author="Ditra Software Srl",
	author_email="admin@ditra.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
