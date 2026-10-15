from setuptools import setup, find_packages

setup(
    name="clinic",
    version="4.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "prettytable",
        "google-auth",
        "google-auth-httplib2",
        "google-auth-oauthlib",
        "google-api-python-client",
    ],
    entry_points={
        "console_scripts": [
            "clinic=src.commands.clinic:cli",
        ],
    },
)