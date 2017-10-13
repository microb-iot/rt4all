#! /usr/bin/env python
"""
Example sending the "Hello World" message using the raw function
of the Modbus module. To verify it's operation, you must connect
the PC and Ivy to the same rs485 network and run it on the PC
../tools/snifferPort.py before launching this script.
"""

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

    m.raw(tx)

    print 'Sent'
