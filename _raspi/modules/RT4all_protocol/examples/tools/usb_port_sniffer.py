#! /usr/bin/env python
"""
USB port sniffer
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

import modbus

if __name__ == '__main__':
    response = None
    m = modbus.Modbus(
        baudrate = 9600,
        parity = 'N',
        stopbits = 1)
    serial = m.get_serial()

    print 'Starting...'

    if serial:
        print 'Serial', serial
        while True:
            response = list(m.read())
            if response:
                print '--- Response ---'
                print 'Number of bytes:', len(response)
                print response
                print '--- ---'
                response = None
    else:
        print 'Error while trying to establish communication'
