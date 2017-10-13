#! /usr/bin/env python

"""
rt4all_protocol module
"""

__author__ = 'Juan Carlos Chaves'
__copyright__ = 'Copyright (C) 2017'
__license__ = 'MIT (expat) License'
__version__ = '1.0'
__maintainer__ = 'Juan Carlos Chaves Puertas'
__email__ = 'lobolanja@gmail.com.com'


import sys
import os
import serial
import struct
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



DEFAULT_PORT = '/dev/ttyACM0'

BAUDRATE_2400 = 2400
BAUDRATE_4800 = 4800
BAUDRATE_9600 = 9600
BAUDRATE_19200 = 19200
BAUDRATE_38400 = 38400
BAUDRATE_57600 = 57600
BAUDRATE_115200 = 115200




COLON = '\x35'
CARRIAGE_RETURN = '\x0D'
LINE_FEED = '\x0A'

BYTE_MAX_FRAME = 255    #: Maximum frame
FRAME_END = 3.5
FRAME_END_ASCII = CARRIAGE_RETURN + LINE_FEED


ALL_BAUDRATE = [BAUDRATE_2400, BAUDRATE_4800, BAUDRATE_9600, BAUDRATE_19200, BAUDRATE_38400, BAUDRATE_57600, BAUDRATE_115200] #: Baud rate support
ALL_PARITY = [serial.PARITY_NONE, serial.PARITY_ODD]        #: Parity support
ALL_STOPBITS = [serial.STOPBITS_ONE, serial.STOPBITS_TWO]   #: Stop bits support
ALL_BYTESIZE = [serial.EIGHTBITS]                           #: Bytesize support


DEFAULT_BAUDRATE = ALL_BAUDRATE[2]      #: Baud rate default
DEFAULT_PARITY = ALL_PARITY[0]          #: Parity default
DEFAULT_STOPBITS = ALL_STOPBITS[0]      #: Stop bits default
DEFAULT_BYTESIZE = ALL_BYTESIZE[0]      #: Bytesize default
DEFAULT_TIMEOUT = None                  #: Timeout default
DEFAULT_DELAY = 0                       #: Delay default

BYTE_PER_SEC_2400 = 0.0046              #: Seconds to transfer a byte to 2400 baud
BYTE_PER_SEC_4800 = 0.0023              #: Seconds to transfer a byte to 4800 baud
BYTE_PER_SEC_9600 = 0.0012              #: Seconds to transfer a byte to 9600 baud
BYTE_PER_SEC_19200 = 0.000573           #: Seconds to transfer a byte to 19200 baud
BYTE_PER_SEC_38400 = 0.000286           #: Seconds to transfer a byte to 38400 baud
BYTE_PER_SEC_57600 = 0.000177           #: Seconds to transfer a byte to 57600 baud
BYTE_PER_SEC_115200 = 0.00095           #: Seconds to transfer a byte to 115200 baud

class RT4all_protocol:
    """"""
    def __init__(self, port = DEFAULT_PORT, baudrate = DEFAULT_BAUDRATE, bytesize = DEFAULT_BYTESIZE, parity = DEFAULT_PARITY, stopbits = DEFAULT_STOPBITS, timeout = None, delay = DEFAULT_DELAY):
        """
        :param port: Port
        :param baudrate: Baud rate
        :param bytesize: Number of data bits
        :param parity: Enable parity checking
        :param stopbits: Number of stop bits
        :param timeout: Set a read timeout value
        :param delay: Set a read delay value


        :type port: string
        :type baudrate: integer
        :type bytesize: integer
        :type parity: char
        :type stopbits: integer
        :type timeout: float
        :type delay: float
      
        """
        
        self.serial = None

        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits

        if timeout == None:
            self.timeout = self.get_time_transfer(BYTE_MAX_FRAME, self.baudrate)
        else:
            self.timeout = timeout

        self.delay = delay
        

        self.set_serial(self.port, self.baudrate, self.bytesize, self.parity, self.stopbits, self.timeout, self.delay)

    def set_serial(self, port = None, baudrate = None, bytesize = None, parity = None, stopbits = None, timeout = None, delay = None):
        """
        Create a new pySerial.
        Default timeout is get_time_transfer(255, baudrate)
        pySerial.timeout = (timeout + delay)

        :param port: Port
        :param baudrate: Baud rate
        :param bytesize: Number of data bits
        :param parity: Enable parity checking
        :param stopbits: Number of stop bits
        :param timeout: Set a read timeout value
        :param delay: Set a read delay value

        :type port: string
        :type baudrate: integer
        :type bytesize: integer
        :type parity: char
        :type stopbits: integer
        :type timeout: float
        :type delay: float

        :returns: Serial
        :rtype: pySerial, None
        """
        self.serial_close()

        if not port == None:
            self.port = port

        if not baudrate == None:
            self.baudrate = baudrate

        if not bytesize == None:
            self.bytesize = bytesize

        if not parity == None:
            self.parity = parity

        if not stopbits == None:
            self.stopbits = stopbits

        if not timeout == None:
            self.timeout = timeout

        if not delay == None:
            self.delay = delay

       

        try:
            self.serial = serial.Serial(
                port = self.port,
                baudrate = self.baudrate,
                bytesize = self.bytesize,
                parity = self.parity,
                stopbits = self.stopbits,
                timeout = 0.2 #(self.timeout + self.delay)
            )
            return self.serial

        except Exception as e:
            print 'Serial exception', e
            self.serial = None

    def set_port(self, port = DEFAULT_PORT):
        """
        If pySerial already existed modify port else create a new pyserial with default values and new port

        :param port: Port
        :type port: string

        :returns: Serial
        :rtype: pySerial
        """
        return self.set_serial(port = port)

    def set_baudrate(self, baudrate = DEFAULT_BAUDRATE):
        """
        If pySerial already existed modify baudrate else create a new pyserial with default values and new baudrate

        :param baudrate: Baud rate
        :type baudrate: integer

        :returns: Serial
        :rtype: pySerial
        """
        return self.set_serial(baudrate = baudrate)

    def set_bytesize(self, bytesize = DEFAULT_BYTESIZE):
        """
        If pySerial already existed modify bytesize else create a new pyserial with default values and new bytesize

        :param bytesize: Number of data bits
        :type bytesize: integer

        :returns: Serial
        :rtype: pySerial
        """
        return self.set_serial(bytesize = bytesize)

    def set_parity(self, parity = DEFAULT_PARITY):
        """
        If pySerial already existed modify parity else create a new pyserial with default values and new parity

        :param parity: Enable parity checking
        :type parity: char

        :returns: Serial
        :rtype: pySerial
        """
        return self.set_serial(parity = parity)

    def set_stopbits(self, stopbits = DEFAULT_STOPBITS):
        """
        If pySerial already existed modify stopbits else create a new pyserial with default values and new stopbits

        :param stopbits: Number of stop bits
        :type stopbits: integer

        :returns: Serial
        :rtype: pySerial
        """
        return self.set_serial(stopbits = stopbits)

    def set_timeout(self, timeout = DEFAULT_TIMEOUT):
        """
        If pySerial already existed modify timeout else create a new pyserial with default values and new timeout

        :param timeout: Set a read timeout value
        :type timeout: float

        :returns: Serial
        :rtype: pySerial
        """
        return self.set_serial(timeout = timeout)

    def set_delay(self, delay = DEFAULT_DELAY):
        """
        If pySerial already existed modify delay else create a new pyserial with default values and new delay

        :param delay: Set a read delay value
        :type delay: float

        :returns: Serial
        :rtype: pySerial
        """
        return self.set_serial(delay = delay)


    def get_serial(self):
        """
        :returns: Serial
        :rtype: pySerial
        """
        return self.serial

    def get_port(self):
        """
        :returns: Port pySerial
        :rtype: string, None
        """
        if self.serial:
            return self.serial.port

    def get_baudrate(self):
        """
        :returns: Baud rate pySerial
        :rtype: integer, None
        """
        if self.serial:
            return self.serial.baudrate

    def get_bytesize(self):
        """
        :returns: Number of data bits pySerial
        :rtype: integer, None
        """
        if self.serial:
            return self.serial.bytesize

    def get_parity(self):
        """
        :returns: Parity pySerial
        :rtype: char, None
        """
        if self.serial:
            return self.serial.parity

    def get_stopbits(self):
        """
        :returns: Number of stop bits pySerial
        :rtype: integer, None
        """
        if self.serial:
            return self.serial.stopbits

    def get_timeout(self):
        """
        :returns: Timeout
        :rtype: float, None
        """
        if self.serial:
            return self.timeout

    def get_delay(self):
        """
        :returns: Delay
        :rtype: float, None
        """
        if self.serial:
            return self.delay

    def get_protocol(self):
        """
        :returns: Protocol
        :rtype: string
        """
        return self.protocol

    def get_supported_parity(self):
        """
        :returns: All supported parity
        :rtype: Array (integer)
        """
        return ALL_PARITY

    def get_supported_stopbits(self):
        """
        :returns: All supported stopbits
        :rtype: Array (integer)
        """
        return ALL_STOPBITS

    def get_supported_protocol(self):
        """
        :returns: All supported Protocol
        :rtype: Array (string)
        """
        return ALL_PROTOCOL

    def get_supported_baudrate(self):
        """
        :returns: All supported baudrate
        :rtype: Array (integer)
        """
        return ALL_BAUDRATE

    def get_supported_bytesize(self):
        """
        :returns: All supported bytesize
        :rtype: Array (integer)
        """
        return ALL_BYTESIZE

    def get_time_transfer(self, tx_bytes=0, baud=None):
        """
        :param tx_bytes: Number of byte to transfer
        :param baud: Baud rate to transfer. If baud is None, get_baudrate()

        :type tx_bytes: float
        :type baud: integer, None

        :returns: Seconds to transfer, -1 if baud not supported
        :rtype: float
        """
        result = -1

        if baud == None:
            baud = self.get_baudrate()

        if baud == BAUDRATE_2400:
            result = tx_bytes*BYTE_PER_SEC_2400
        elif baud == BAUDRATE_4800:
            result = tx_bytes*BYTE_PER_SEC_4800
        elif baud == BAUDRATE_9600:
            result = tx_bytes*BYTE_PER_SEC_9600
        elif baud == BAUDRATE_19200:
            result = tx_bytes*BYTE_PER_SEC_19200
        elif baud == BAUDRATE_38400:
            result = tx_bytes*BYTE_PER_SEC_38400
        elif baud == BAUDRATE_57600:
            result = tx_bytes*BYTE_PER_SEC_57600
        elif baud == BAUDRATE_115200:
            result = tx_bytes*BYTE_PER_SEC_115200

        return result

    def get_time_silent(self, baud=None):
        """
        :param baud: Baud rate to transfer. If baud is None, get_baudrate()
        :type baud: integer, None

        :returns: Call `self.get_time_transfer(3.5)`
        :rtype: float
        """
        return self.get_time_transfer(FRAME_END, baud)

    def raw(self, tx, byte_read = 255):
        """
        :param tx: Buffer to transfer
        :param byte_read: Number of bytes to read

        :type tx: Bytes
        :type byte_read: integer

        :returns: Response
        :rtype: Buffer of bytes, None
        """
        self.write(tx)
        self.sleep_tx(len(tx))
        return self.read(byte_read)

    def write(self, tx):
        """
        :param tx: Buffer to transfer
        :type tx: Buffer of bytes

        :returns: Number of byte written
        :rtype: int, None
        """
        if self.serial:
            try:
                return self.serial.write(tx)
            except Exception as e:
                print 'Write exception', e
                # self.serial_close()

    def read(self, num_bytes=255):
        """
        :param num_byte: Number of bytes to read
        :type num_byte: integer

        :returns: Buffer of bytes readed
        :rtype: Buffer of bytes, None
        """
        if self.serial:
            try:
                return self.serial.read(num_bytes)
            except Exception as e:
                print 'Read exception', e
               

    def sleep_tx(self, num_bytes):
        """
        Call `time.sleep(get_time_transfer(num_byte))`

        :param num_byte: Number of bytes to write
        :type num_byte: integer
        """
        time.sleep(self.get_time_transfer(num_bytes))

    
    def serial_close(self):
        """
        Close pySerial
        """
        if self.serial:
            self.serial.close()

        self.serial = None

    def __del__(self):
        """"""
        self.serial_close()


if __name__ == "__main__":
    """"""     
m = RT4all_protocol()
tx = '\x01\x06\x00\x06\x00\x01'
rx = m.raw(tx)
print list(tx)
print list(rx)
#for i in range[1,255]:
time.sleep(0.01)
	

#tx = '\x01\x03\x00\x00\x00\x02'
tx = '\x01\x06\x00\x06\x00\x00'
rx = m.raw(tx)
print list(tx)
print list(rx)
