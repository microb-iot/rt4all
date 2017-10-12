#! /usr/bin/env python

"""
Example in which it runs a script that sends a greeting
from Ivy to the PC, then Ivy receives a greeting from the PC.
To finish Ivy says goodbye to the PC and the PC says
goodbye to Ivy, after the above the script ends.
Is necessary to run DonPepito.py first and then Run DonJose.py
Device: Ivy
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

import rs485     # set_tx_enable / set_rx_enable

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
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.5)

    print s

    rs485.set_tx_enable()
    s.write("Hola Don Pepito")
    t_sleep = len("Hola Don Pepito")*BYTE_PER_SEC_9600
    time.sleep(t_sleep)
    rs485.set_rx_enable()
    acabado = False
    while not acabado:
        response = s.read(byte_read)
        if response == "Hola Don Jose":
            print "Don Pepito: Hola Don Jose"
            rs485.set_tx_enable();
            s.write("Adios Don Pepito")
            t_sleep = len("Adios Don Pepito")*BYTE_PER_SEC_9600
            time.sleep(t_sleep)
            response = None
            rs485.set_rx_enable();

        if response == "Adios Don Jose":
            print "Don Pepito: Adios Don Jose"
            print "FIN"
            response = None
            rs485.set_rx_enable();
            acabado = True
