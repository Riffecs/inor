import io
import os
import setuptools


def read_description():
    url = "README.md"
    """ Read and Return the description """
    return io.open(
        os.path.join(os.path.dirname(__file__), url), encoding="utf-8"
    ).read()


def def_requirements():
    """Check PIP Requirements"""
    with open("requirements.txt", encoding="utf-8") as file_content:
        pip_lines = file_content.read().splitlines()
    return pip_lines


setuptools.setup(
    name="inor",
    version="0.0.5",
    description="Package Manager Backend",
    entry_points={"console_scripts": ["inor=inor:handler"]},
    data_files=[("man/man1", ["man/inor.1"])],
    long_description=read_description(),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="Package Manager Backend - inor",
    url="https://github.com/Riffecs/inor",
    packages=["inor"],
    install_requires=def_requirements(),
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
