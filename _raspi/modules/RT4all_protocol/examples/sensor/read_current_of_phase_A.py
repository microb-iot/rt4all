"""
Example to read the transducer's name and configuration

Device:
Digital transducer
Model: CE-AD11B-32ES5
http://www.ce-transducer.com/product/details/182/131/details

TX
Addres of slave:                01h
Function code:                  03h
Addres of the first register:   0011h
Quanty of registers:            0001h
CRC:                            0401h

RX
Addres of slave:                1 Byte
Function code:                  1 Byte
Byte count:                     1 Byte
Value                           2 Bytes
CRC:                            2 Bytes
"""

__author__ = 'Javi Ortega'
__copyright__ = 'Copyright (C) 2017'
__license__ = 'MIT (expat) License'
__version__ = '0.1'
__maintainer__ = 'Javi Ortega'
__email__ = 'javier.ortega@whitewallenergy.com'


import struct
import sys
import os

module_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, module_path)


if __name__ == '__main__':
    """"""
    import modbus
    m = modbus.Modbus(
        baudrate = 9600,
        parity = 'N',
        stopbits = 1)

    slave = '\x01'
    code_read = '\x03'
    start_address = '\x00\x11'
    num_of_registers = '\x00\x01'

    tx = slave + code_read + start_address + num_of_registers
    tx += m.get_crc(tx)

    rx = m.raw(tx)

    if rx:
        print 'Current of phase A', struct.unpack('<H', rx[3:len(rx)-2])[0]
    else:
        print 'Without response'
