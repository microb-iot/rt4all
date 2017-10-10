#! /usr/bin/env python
"""

Example Loop test to check communication.

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

    tx = '\x01\x08\x00\x00\x01\xF4\xE0\x1C'
    print "TX\n"
    print list(tx) #'\x01\x08\x00\x00\x01\xF4\xE0\x1C'

    rx = m.raw(tx)

    if rx:
        print "RX\n"
        print list(rx)
    else:
        print 'Without response'
