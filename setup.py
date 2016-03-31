"""
Useful Utils
==============

"""

from setuptools import setup, find_packages

setup(
    name='utilitybelt',
    version='0.2.6',
    author='Halfmoon Labs',
    author_email='hello@halfmoonlabs.com',
    description='Generally useful tools. A python utility belt.',
    keywords=('dict dictionary scrub to_dict todict json characters charset '
              'hex entropy utility'),
    url='https://github.com/onenameio/utilitybelt',
    license='MIT',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
