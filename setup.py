from pathlib import Path

from setuptools import find_packages, setup


README_PATH = Path(__file__).parent / "README.md"

setup(
    name="awlise",
    version="1.0.0",
    author="Awakno",
    author_email="contact@awakno.fr",
    description="An awmazing API wrapper for Alise.",
    long_description=README_PATH.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/Awakno/Awlise",
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
        "pydantic",
    ],
    include_package_data=True,
)
