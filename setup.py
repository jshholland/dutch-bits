#!/usr/bin/env python

from distutils.core import setup

setup(
        name='dutch-bits',
        version='0.2',
        description='Homebrew Python toolkit. Use at your own risk :)',
        author='Josh Holland',
        author_email='jrh@joshh.co.uk',
        url='http://github.com/jshholland/pytools.git',
        classifiers = [
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Utilities',
        ],
        py_modules = ['inflist'],
        scripts = ['fpi.py'],
 )
