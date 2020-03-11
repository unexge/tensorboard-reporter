# type: ignore

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tensorboard-reporter",
    version="0.0.3",
    author="unexge",
    author_email="unexge@gmail.com",
    description="Get reports for your training process via Slack",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unexge/tensorboard-reporter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    scripts=["bin/tensorboard-reporter"],
)
