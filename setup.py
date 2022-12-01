from setuptools import setup, find_packages

with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name="adventofcode-2022",
    version="1.0",
    description="Advent of code 2022",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "prepare=cli:prepare",
            "test-sol=cli:test",  # We can't use `test`
            "solve=cli:solve",
            "submit=cli:submit",
        ]
    },
)
