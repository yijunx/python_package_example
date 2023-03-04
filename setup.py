from setuptools import find_packages, setup

with open("app/Readme.md", "r") as fh:
    long_description = fh.read()


setup(
    name="idgenerator",
    version="0.0.1",
    description="A package to generate random IDs",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="some github location",
    author="John Doe",
    author_email="j@j.com",
    license="MIT",
    classifiers=[
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={"dev": ["pytest>=7.0", "twine>=4.0.2"]}, #twine is used for publish to pypi or somewhere else..
    python_requires=">=3.10",
)
