import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="DataBorealis",
    version="1.0.0",
    description="Localized, file-based database module.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/EKHolmes/DataBorealis/",
    author="Erik Holmes",
    author_email="zv.eevee6718@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)