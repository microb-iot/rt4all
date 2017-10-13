#! /usr/bin/env python

"""
Example to enable GPIO: direction OUT and value HIGH

Device: Ivy
"""

__author__ = 'Javi Ortega'
__copyright__ = 'Copyright (C) 2017'
__license__ = 'MIT (expat) License'
__version__ = '0.1'
__maintainer__ = 'Javi Ortega'
__email__ = 'javier.ortega@whitewallenergy.com'

import sys
import os

module_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, module_path)

import gpio

A_GPIO = 23

if __name__ == '__main__':
    """"""
    g = gpio.Gpio()
    g.setup()

    g.output(A_GPIO)
    g.set(A_GPIO)
