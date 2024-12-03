import os

from setuptools import setup, find_packages


def read_requirements(filename):
    """Read requirements from a file."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as file:
        return file.read().splitlines()


setup(
    name="auto-ninja",
    version="0.1.0",
    packages=find_packages(),
    install_requires=read_requirements("requirements/production.txt"),
    entry_points={
        "console_scripts": [
            "auto-ninja=auto_ninja.main:main",
        ],
    },
    author="Sascha Krug",
    author_email="sascha@fa-krug.de",
    description="Auto Ninja is a Python library for Django developers that automates the generation of API structures, reducing setup time and enhancing productivity.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fa-krug/auto-ninja",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
)
