#!/usr/bin/env python
from setuptools import setup, find_packages
import my_rss_reader

setup(
    name="rss_reader",
    version=my_rss_reader.__version__,
    description="Pure command-line RSS reader",
    author="Volha Zayanchkouskaya",
    author_email="ollya_92@mail.ru",
    packages=['my_rss_reader'],
    include_package_data=True,
    install_requires=['bs4', 'lxml', 'requests', 'fpdf', 'pandas',
                      'python-dateutil', 'setuptools', 'wheel'],
    python_requires=">=3.9",
    entry_points={
        'console_scripts': ['rss_reader = my_rss_reader.rss_reader:main']
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
