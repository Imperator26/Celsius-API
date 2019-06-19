import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="celsius",
    version="0.1.4",
    author="Federico A. Corazza",
    author_email="federico.corazza@live.it",
    description="A Python wrapper for the Celsius API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Imperator26/Celsius-API",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
