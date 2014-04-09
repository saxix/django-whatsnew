#!/usr/bin/env python
from setuptools import setup, find_packages

dirname = 'whatsnew'

app = __import__(dirname)

setup(
    name=app.NAME,
    version=app.get_version(),
    url='https://github.com/saxix/django-whatsnew',
    description="Simple application to manage `what's new` screen.",
    author='sax',
    author_email='sax@os4d.org',
    license='BSD',
    packages=find_packages('.'),
    include_package_data=True,
    platforms=['linux'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers'
    ]
)
