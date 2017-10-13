#! /usr/bin/env python
"""
Example read coil.

Device: Variable Frequency Drives
Model: MX2-series
See documentation (https://assets.omron.eu/downloads/manual/en/i570_mx2_users_manual_en.pdf)
"""

__author__ = 'Juan Carlos Chaves'
__copyright__ = 'Copyright (C) 2017'
__license__ = 'MIT (expat) License'
__version__ = '0.1'
__email__ = 'juan.chaves@whitewallenergy.com'

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import modbus

if __name__ == '__main__':
    m = modbus.Modbus(
        baudrate = 9600,
        parity = 'N',
        stopbits = 1)
    tx = '\x01\x01\x00\x06\x00\x05\x1C\x08'
    print "TX\n"
    print list(tx)

    rx = m.raw(tx)

    if rx:
        print "RX\n"
        print list(rx)
    else:
        print 'Without response'
