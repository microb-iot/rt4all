"""
Example to read the transducer's name and configuration

Device:
Digital transducer
Model: CE-AD11B-32ES5
http://www.ce-transducer.com/product/details/182/131/details

TX
Addres of slave:                01h
Function code:                  03h
Addres of the first register:   0010h
Quanty of registers:            000Ah
CRC:                            C408h

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

import time
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
    start_address = '\x00\x10'
    num_of_registers = '\x00\x0A'

    tx = slave + code_read + start_address + num_of_registers
    tx += m.get_crc(tx)

    while True:
        result = []
        rx = None

        rx = m.raw(tx)
        # rx = '\x01\x03\x14\x00\x00\x80\x00\x80\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\xEC\xC7'

        # print 'tx', list(tx)
        # print 'rx', list(rx)

        for v in [rx[i:i+2] for i in range(3, len(rx)-2, 2)]:
            result.append(struct.unpack('<H', v)[0])

        if len(result) == 10:
            print '----- MEASUREMENT -----'
            print 'Voltage of phase A', result[0]
            print 'Current of phase A', result[1]
            print 'Voltage of phase B', result[2]
            print 'Current of phase B', result[3]
            print 'Voltage of phase C', result[4]
            print 'Current of phase C', result[5]
            print 'P: active power', result[6]
            print 'Q: reactive power', result[7]
            print 'Cos: power factor', result[8]
            print 'F: frequency', result[9]

        time.sleep(1)
