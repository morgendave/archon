import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tristan",
    version="0.0.1",
    author="Zhiwei Zhao",
    author_email="morgendave@gmail.com",
    description="Ulysses, an another python async job management and report framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/morgendave/tristan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)