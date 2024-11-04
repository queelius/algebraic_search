from setuptools import setup, find_packages

setup(
    name="algebraic_search",
    version="0.1.0",
    description="A description of my package",
    author="Alex Towell",
    author_email="lex@metafunctor.com",
    url="https://github.com/queelius/algebraic_search",  # GitHub or other repo URL
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        # Add dependencies here, e.g., "numpy>=1.21.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
