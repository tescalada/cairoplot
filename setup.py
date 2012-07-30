#!/usr/bin/env python
'''Cairoplot installation script.'''

from distutils.core import setup
import os

setup(
    description='Cairoplot',
    license='GNU LGPL 2.1',
    long_description='''
        Using Python and PyCairo to develop a module to plot graphics in an
        easy and intuitive way, creating beautiful results for presentations, 
        websites and papers.
        ''',
    name='CairoPlot',
    packages=['cairoplot'],
    author='Rodrigo Araujo',
    author_email='cairoplot [at] googlegroups [dot] com',
    url='http://rodrigoaraujo01.github.com/cairoplot/',
    version='1.2',
    )

