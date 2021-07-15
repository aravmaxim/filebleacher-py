import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="filebleacher-py",
    version="0.0.1",
    author="Maxim Arav",
    author_email="aravmaxim@gmail.com",
    description="Implamenting FileBleacher for python. Its an open source CDR project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aravmaxim/filebleacher-py",
    project_urls={
        "Bug Tracker": "https://github.com/aravmaxim/filebleacher-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)