# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

extra = {}

with open('README.md', 'rt') as f:
    extra['long_description'] = f.read()

setup(
    name='dash-id-utils',
    version='0.0.2',
    description='',
    author='mapix',
    author_email='mapix.me@gmail.com',
    url='https://github.com/pragmatic-dash/dash-id-utils',
    license='MIT',
    packages=find_packages(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=['dash'],
    **extra
)