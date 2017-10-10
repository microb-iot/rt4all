#! /usr/bin/env python

"""
The PC is until it receives a greeting from the Ivy. Then answer with
another greeting to Ivy. To finish Ivy says goodbye to the PC and
the PC says goodbye to Ivy, after the above the script ends.
You need to run DonPepito.py first and then Run DonJose.py

Device: PC
"""

__author__ = 'Juan Carlos Chaves'
__copyright__ = 'Copyright (C) 2017'
__license__ = 'MIT (expat) License'
__version__ = '0.1'
__email__ = 'juan.chaves@whitewallenergy.com'

import serial
import sys
import os
import platform
import time

module_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, module_path)

import rs485     # set_tx_enable() / set_rx_enable()

DIR_SERIAL_PORT_MIPS = '/dev/ttyATH0'
DIR_SERIAL_PORT_LINUX = '/dev/ttyUSB0'
PLATFORM_MIPS = 'mips' == platform.machine()
BYTE_PER_SEC_9600 = 0.0012
BAUD_INIT = 9600
rs485 = rs485.Rs485()

if __name__ == '__main__':
    response = None
    byte_read = 1024
    s = serial.Serial(
        port=DIR_SERIAL_PORT_MIPS if PLATFORM_MIPS else DIR_SERIAL_PORT_LINUX,
        baudrate=BAUD_INIT,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.5)

    print s
    acabado = False
    while not acabado:
        response = s.read(byte_read)
        if response=="Hola Don Pepito":
            print "Don Jose: Hola Don Pepito"
            s.write("Hola Don Jose")
            t_sleep = len("Hola Don Jose")*BYTE_PER_SEC_9600
            time.sleep(t_sleep)
            response = None
        if response == "Adios Don Pepito":
            print "Don Jose: Adios Don Pepito"
            s.write("Adios Don Jose")
            print "FIN"
            response = None
            acabado = True
