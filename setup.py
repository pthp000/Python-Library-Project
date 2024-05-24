from setuptools import setup, find_packages

setup(
    name='Lx-Pytn',
    version='0.2.1',
    author='AhmadA AsmaKh AmalSb',
    author_email='pythonprojectg@gmail.com',
    description='A comprehensive Python library for data preprocessing',
    url='https://github.com/pthp000',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'sklearn',
        'nltk',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)