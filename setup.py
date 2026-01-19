from setuptools import setup, find_packages

setup(
    name="recon-tool",
    version="1.0.0",
    description="Automated reconnaissance and attack surface mapping CLI tool",
    author="Omini Vishwakarma",
    packages=find_packages(),
    py_modules=["recon_tool"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "recon=recon_tool:main",
        ]
    },
)
