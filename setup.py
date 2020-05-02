import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sudoku-create",
    version="0.1",
    description="A Python package to create a pair of solve and unsolve sudoku.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kush-savani/Sudoku.git",
    author="Kaushal Savani",
    author_email="kaushalsavani@gmail.com",
    license = "MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    include_package_data = True,
    packages=["sudoku"],
    python_requires='>=3',
) 
