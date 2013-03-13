# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

description = """
django-pipeline i18next that takes translation files in YML format and adds them to the javascript namespace.
"""

setup(
  name='django-pipeline-i18next',
  version='0.1.1',
  description=description,
  long_description=description,
  author='Jared Scott',
  author_email='gecko@uw.edu',
  url='https://github.com/gcko/django-pipeline-i18next',
  packages=find_packages(),
  zip_safe=False,
  install_requires=['PyYAML==3.10'],
  include_package_data=True,
  classifiers=[
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Utilities',
    ]
)