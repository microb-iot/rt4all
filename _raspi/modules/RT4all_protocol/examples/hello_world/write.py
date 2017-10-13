#! /usr/bin/env python
"""
Example that sends the message "Hello World" using Modbus module,
but without using the raw function. To verify it's operation,
you must connect the PC and Ivy to the same rs485 network and
run it on the PC ../tools/snifferPort.py before launching this script.

Devices : Ivy and PC

"""

__author__ = 'Juan Carlos Chaves'
__copyright__ = 'Copyright (C) 2017'
__license__ = 'MIT (expat) License'
__version__ = '0.1'
__email__ = 'juan.chaves@whitewallenergy.com'

import sys
import os

module_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, module_path)

import modbus

if __name__ == '__main__':
    m = modbus.Modbus(
        baudrate = 9600,
        parity = 'N',
        stopbits = 1)

    tx = 'Hello_word'

    m.set_tx_enable()
    m.write(tx)
    m.sleep_tx(len(tx))

    print 'Sent'
