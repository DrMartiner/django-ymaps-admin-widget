# -*- coding: utf-8 -*-

import os
from distutils.core import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ymaps-admin-widget',
    version='1.0.9',
    packages=['yandexmaps_widget'],
    url='https://github.com/DrMartiner/django-ymaps-admin-widget',
    license='MIT',
    author='Alexey Kuzmin',
    author_email='DrMartiner@GMail.Com',
    description='Widget admin for Yandex Maps',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.3',
        'psycopg2',
    ],
)