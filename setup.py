from datetime import datetime
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = datetime.now().strftime("%Y.%m.%d.%H.%M.%S")

setuptools.setup(
    name="hotreload", # Replace with your own username
    version=version,
    author="Sayan Goswami",
    author_email="me@sayan.page",
    description="Run any arbitrary python script every time the code changes in the file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/say4n/hotreload.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)