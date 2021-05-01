from os import path
from setuptools import setup

# read the contents of your description file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'description.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="tigopesa",
    version="0.1",
    description="A python wrapper for Tigopesa Payment API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Kalebu/tigopesa",
    download_url="https://github.com/Kalebu/tigopesa/archive/0.1.tar.gz",
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["tigopesa"],
    keywords=[
        "tigopesa payments",
        "mobile payments"
        "python-tigopesa package"
        "tigopesa-python"
        "tanzania",
        "python-tanzania",
    ],
    install_requires=[
        'pydantic',
        'requests',
    ],
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
