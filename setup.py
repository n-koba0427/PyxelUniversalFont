from setuptools import setup, find_packages

setup(
    name="pyxel-universal-font",
    version="1.0.1",
    packages=find_packages(),
    package_data={'PyxelUniversalFont': ['fonts/*']},
    install_requires=[
        "numpy",
        "Pillow",
        "pyxel",
    ],
    author="naoyashi",
    author_email="n.koba0427@gmail.com",
    description='An extension tool to add fonts to the public "pyxel" library.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/n-koba0427/PyxelUniversalFont",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Japanese",
    ],
    entry_points={
        'console_scripts': [
            'puf=PyxelUniversalFont.command:command_manager',
        ],
    },
)
