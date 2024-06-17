'''
MIT License

Copyright (c) 2020 Jimeno Fonseca

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os

from setuptools import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()

here = os.path.abspath(os.path.dirname(__file__))
_version = {}
_version_path = os.path.join(here, 'model', '__init__.py')
with open(_version_path, 'r') as f:
    exec(f.read(), _version)

install_requires = ['numpy==1.16.0',
                    'pandas==0.23.4',
                    'enthalpygradients==1.0'
                    'pymc3==3.6',
                    'scikit-learn==1.5.0'
                    ]

setup(
    name='HBLM-USA',
    version=_version['__version__'],
    packages=['HBLM-USA'],
    url='https://github.com/JIMENOFONSECA/bsts-sg',
    license='MIT',
    author='Jimeno Fonseca',
    author_email='fonseca.jimeno@gmail.com',
    description="HBLM-USA: forecasting model based on Hierarchical Bayesian Linear Model for Climate Change Impact Scenarios in the USA",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"]
)
