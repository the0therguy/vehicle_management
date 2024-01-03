from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vehicle_management/__init__.py
from vehicle_management import __version__ as version

setup(
	name="vehicle_management",
	version=version,
	description="Vehicle Management",
	author="Ami",
	author_email="ami@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
