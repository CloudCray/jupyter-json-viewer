#!/usr/bin/env python

from setuptools import setup

setup(
    name='jupyter_json_viewer',
    version='0.1.0',
    description='Jupyter extension to display/explore JSON data structures',
    author='Cloud Cray',
    author_email='cloud@patientprice.com',
    url='https://github.com/CloudCray/jupyter-json-viewer',
    packages=[
        'jupyter_json_viewer',
    ],
    include_package_data=True,
    install_requires=[
        "IPython>=3.0.0",
    ],
    classifiers=[
        'Development Status :: 0 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)