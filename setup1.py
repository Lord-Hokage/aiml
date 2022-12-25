import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="forbiddenLab",
    version="0.0.2",
    author="zenitsu",
    author_email="zenitsu017@gmail.com",
    description="all 7th sem aiml programs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnmolKamat/aiml",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
