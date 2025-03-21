from setuptools import setup, find_packages

setup(
    name="awlise",
    version="0.1.0",
    author="LiterateInk",
    author_email="contact@literate.ink",
    description="An awmazing API wrapper for Alise.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LiterateInk/Awlise",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "aiohttp",
        "beautifulsoup4",
    ],
    include_package_data=True,
)
