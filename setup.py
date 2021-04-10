from setuptools import setup
import imp

with open('README.md') as file:
    long_description = file.read()

version = imp.load_source('datasets.version', 'datasets/version.py')

setup(
    name='datasets',
    version=version.version,
    description='A library for datasets',
    author='Russell Izadi',
    author_email='russell.izadi@gmail.com',
    url='https://github.com/russellizadi/datasets',
    download_url='http://github.com/russellizadi/datasets/releases',
    packages=['datasets'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='dataset audio',
    license='BSD-3-Clause',
    classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.6",
        ],
    install_requires=[
        'numpy>=1.20.2',
        'soundfile',
    ],
    extras_require={
        'tests': ['backports.tempfile', 'pytest', 'pytest-cov', 'tqdm']
    }
)