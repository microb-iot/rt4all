"""

Example to write the transducer's name and configuration
address (0-256)
baudrate (3-7) | values (3-->1200), (4-->2400), (5-->4800), (6-->9600), (7-->19200).

Device:
Digital transducer
Model: CE-AD11B-32ES5
See documentation (http://www.ce-transducer.com/down/CE-A-catalog.pdf)
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

    rx = m.raw('\x01\x10\x00\x20\x00\x01\x02\x01\x06\x20\xA2')
    #rx "\x01\x10\x00\x20\x00\x01\x00\x03"
    if rx:
        print list(rx)
    else:
        print 'Without response'
