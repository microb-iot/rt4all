"""
Example to read the transducer's name and configuration

Device:
Digital transducer
Model: CE-AD11B-32ES5
http://www.ce-transducer.com/product/details/182/131/details

TX
Addres of slave:                01h
Function code:                  03h
Addres of the first register:   0020h
Quanty of registers:            0003h
CRC:                            0401h

RX
Addres of slave:                01h
Function code:                  03h
Byte count:                     06h
Address of slave:               01h
Baudrate code:                  06h         (9600)
Name:                           44313133h   (D113)
CRC:                            b81eh
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

import modbus

def get_baudrate_value(baudrate_code):
    """
    Translate baurate code to baudrate value

    :param baudrate_code: Baudrate code from rx
    :type baudrate_code: int

    :returns: Baudrate value
    :rtype: int, None
    """
    if baudrate_code == 3:
        return 1200
    elif baudrate_code == 4:
        return 2400
    elif baudrate_code == 5:
        return 4800
    elif baudrate_code == 6:
        return 9600
    elif baudrate_code == 7:
        return 19200

if __name__ == '__main__':
    """"""
    m = modbus.Modbus(
        baudrate = 9600,
        parity = 'N',
        stopbits = 1)

    tx = '\x01\x03\x00\x20\x00\x03\x04\x01'
    rx = m.raw(tx)

    print 'tx', list(tx)

    if rx:
        tmp = list(rx)
        print 'rx', tmp

        print '\nAnalysis of rx'
        print '%sh Addres of slave' % tmp[0].encode('hex')
        print '%sh Function code' % tmp[1].encode('hex')
        print '%sh Byte count' % tmp[2].encode('hex')
        print '%sh Address of slave' % tmp[3].encode('hex')
        print '%sh Baudrate code (%s)' % (tmp[4].encode('hex'), get_baudrate_value(int(tmp[4].encode('hex'))))
        print '%sh First character of the name (%s)' % (tmp[5].encode('hex'), tmp[5])
        print '%sh Second character of the name (%s)' % (tmp[6].encode('hex'), tmp[6])
        print '%sh Third character of the name (%s)' % (tmp[7].encode('hex'), tmp[7])
        print '%sh Fourth character of the name (%s)' % (tmp[8].encode('hex'), tmp[8])
        print '%sh CRC-L' % tmp[9].encode('hex')
        print '%sh CRC-H' % tmp[10].encode('hex')

    else:
        print 'Without response'
