from setuptools import setup, find_packages

setup(
    name="units_conv",  # Your package name
    version="1.0.3",   # Version number
    author="PHR",
    author_email="your.email@example.com",
    description="converts string inputs of electical parameters to equivalent float.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ParuHangRai-PRI/units_conv",
    packages=find_packages(),  # Automatically find all packages
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Python version requirements
)