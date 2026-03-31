from setuptools import setup, find_packages

setup(
    name = "ndfl-",
    version = "0.0.1",
    description="Калькулятор НДФЛ по прогрессивной шкале РФ (2025)",
    long_description=open("README.md", encoding="utf-8").read(),
    url=,
    long_description_content_type = "text/markdown",
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    author = "Shulgin Victor"
)