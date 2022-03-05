from setuptools import setup, find_packages

setup(
    name="dockertop",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["docker", "click", "tabulate"],
    entry_points={"console_scripts": ["dockertop = dockertop.main:main"]},
)
