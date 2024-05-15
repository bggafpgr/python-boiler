from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "mycommand=myproject.module:main",
        ],
    },
)
