#! /usr/bin/env python
"""
Example write and read register

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
    """"""
    m = modbus.Modbus(
        baudrate = 9600,
        parity = 'N',
        stopbits = 1)

    tx = '\x01\x17\x10\x00\x00\x02\x00\x00\x00\x02\x04\x00\x00\x13\x88\xF4\x86'
    print "TX\n"
    print list(tx)
    rx = m.raw(tx)

    if rx:
        print "RX\n"
        print list(rx) #['\x01', '\x17', '\x04', '\x00', '\x00', '\x00', '\x00', '\xf9', "'"]s

    else:
        print 'Without response'
