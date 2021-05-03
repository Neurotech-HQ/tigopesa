import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
long_description = (HERE / "README.md").read_text()

setup(
    name="tigopesa",
    version="0.6",
    description="A python wrapper for Tigopesa Payment API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Kalebu/tigopesa",
    download_url="https://github.com/Kalebu/tigopesa/archive/0.2.tar.gz",
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
