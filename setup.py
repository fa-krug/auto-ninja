from setuptools import setup, find_packages


setup(
    name="auto-ninja",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer==0.14.0",
    ],
    entry_points={
        "console_scripts": [
            "auto-ninja=auto_ninja.main:main",
        ],
    },
    author="Sascha Krug",
    author_email="sascha@fa-krug.de",
    description="Auto Ninja is a Python library for Django developers that automates the generation of API structures, reducing setup time and enhancing productivity.",
    url="https://github.com/fa-krug/auto-ninja",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
