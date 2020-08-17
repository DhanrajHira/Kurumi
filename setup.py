from setuptools import setup, find_packages

setup(
    name="kurumi",
    version="0.3.0",
    license="MIT",
    author="Not Marek, Dhanraj Hira",
    author_email="notmarek@animex.tech",
    description="Animepahe API wrapper.",
    long_description=open("README.md", "r").read(),
    long_description_content="text/markdown",
    url="https://github.com/DhanrajHira/Kurumi",
    packages=find_packages(),
     classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
    
    ]   
)