import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="inputoutput",
    version="0.0.1",
    author="Romashov Vlad",
    author_email="r26101999v@gmail.com",
    description="Package for input and output operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bartholomeow/PythonCode",
    project_urls={
        "Bug Tracker": "https://github.com/Bartholomeow/PythonCode",
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
