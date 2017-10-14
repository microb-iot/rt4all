#! /usr/bin/env python
"""
This class creates the frames and parses the responses.
"""

__author__ = 'Juan Carlos Chaves Puertas'
__copyright__ = 'Copyright (C) 2017'
__license__ = 'MIT (expat) License'
__version__ = '1.0'
__maintainer__ = 'Juan Carlos Chaves Puertas'
__email__ = 'lobolanja@gmail.com'

import struct

# REGISTERS
READ_MULTIPLE_REGISTERS = '\x03'
WRITE_SINGLE_REGISTER = '\x06'





class Frame:
    """"""
    def __init__(self, modbus, slave_address=1, big_endian=True):
        """"""
        self.debug = True
        self.modbus = modbus
        self.big_endian = big_endian
        self.slave_address = self.encode(slave_address, 1)

    def create_frame(self, code_func='\x00', start_address='\x00\x00', data=''):
        """
        Return modbus frame: slave_address + code_func + start_address + data + CRC.

        :param code_func: Buffer of (1) bytes with code function.
        :param start_address: Buffer of (2) bytes with start address.
        :param data: Buffer of bytes with the remaining data.

        :type code_func: Buffer of bytes.
        :type start_address: Buffer of bytes.
        :type data: Buffer of bytes.

        :returns: Modbus frame.
        :rtype: Buffer of bytes.
        """
        tx = self.slave_address + code_func + start_address + data

        return tx 

    def decode(self, hexadecimal='\x00\x00', num_byte=2, endian=True, unsigned=True):
        """
        Decode hexadecimal value to integer value.

        :param hexadecimal: Buffer of bytes to decode.
        :param num_byte: Numer of byte to decode.

        :type hexadecimal: Buffer of bytes.
        :type num_byte: Integer.

        :returns: Decoded value.
        :rtype: Integer.
        """
        return struct.unpack(self.get_format(num_byte, endian, unsigned), hexadecimal)[0]

    def encode(self, integer=0, num_byte=2):
        """
        Encode integer value to hexadecimal value.

        :param hexadecimal: Integer value to encode.
        :param num_byte: Numer of byte to encode.

        :type hexadecimal: Integer.
        :type num_byte: Integer.

        :returns: Encoded value.
        :rtype: Buffer of bytes.
        """

        return struct.pack(self.get_format(num_byte), integer)

    def get_format(self, num_byte=2):
        """
        Get format strings to encode/decode.

        :param num_byte: Numer of byte to encode/decode.
        :param endian:

        :type num_byte: Integer.
        :type endian:

        :returns: Format strings.
        :rtype: String/None.
        """


        fmt = '<' 

        if num_byte == 1:
            fmt += 'B' if unsigned else 'b'
        elif num_byte == 2:
            fmt += 'H' if unsigned else 'h'
        elif num_byte == 4:
            fmt += 'I' if unsigned else 'i'

        return fmt

    ##########
    # FRAMES #
    ##########

    # REGISTERS
    def read_multiple_registers(self, start_address='\x00\x00', num_register=1, unsigned=True):
        """
        Creates a frame to read multiple registers.

        :param start_address: Start address to read.
        :param num_register: Number of registers (max 16).

        :type start_address: Buffer of (2) bytes.
        :type num_register: Integer [1, 16] ( 2 bytes when encode).

        :returns: Frame to read multiple registers.
        :rtype: Buffer of bytes.
        """
        return self.create_frame(READ_MULTIPLE_REGISTERS, start_address, self.encode(num_register, 2, False, unsigned))

    def write_single_register(self, start_address='\x00\x00', value=1, unsigned=True):
        """
        Creates a frame to write single register.

        :param start_address: Start address to write.
        :param value: The new value of register.

        :type start_address: Buffer of (2) bytes.
        :type value: Integer [0, 65535] ( 2 bytes when encode).

        :returns: Frame to write single register.
        :rtype: Buffer of bytes.
        """
        return self.create_frame(WRITE_SINGLE_REGISTER, start_address, self.encode(value, unsigned=unsigned))

   

    

    ###################
    ##### PARSING #####
    ###################

    # REGISTERS
    def parse_read_multiple_registers(self, rx, register_byte=2):
        """
        Translate response frame read multiple registers to array of integers.
        rx: SLAVE (1B) + FUNCTION (\x03 1B) + BYTE DATA (1B) + DATA ([2, 32] B) + CRC (2B)

        :param rx: Response to read multiple registers.
        :param register_byte: Number of byte for each register.

        :type rx: Buffer of bytes.
        :type register_byte: Integer.

        :returns: Array with values of registers.
        :rtype: Array of integers.
        """
        result = []

        if not self.check_error(rx):
            if rx[1] == READ_MULTIPLE_REGISTERS:
                len_rx = len(rx)
                if len_rx >= 7 or len_rx <= 37:
                    for v in [rx[i:i+register_byte] for i in range(3, len(rx)-2, register_byte)]:
                        result.append(self.decode(v, register_byte, unsigned=unsigned))

        return result


    def parse_write_single_register(self, rx, unsigned=True):
        """
        Translate response frame write single registers to integer.
        rx: SLAVE (1B) + FUNCTION (\x06 1B) + START ADDRESS (2B) + DATA (2B) + CRC (2B)

        :param rx: Response to write single register.

        :type rx: Buffer of bytes.

        :returns: Number of registers affected.
        :rtype: Integer.
        """
        result = 0
        if not self.check_error(rx):
            if rx[1] == WRITE_SINGLE_REGISTER:
                if len(rx) == 8:
                    #return self.decode(rx[4:6])
                    result = 1
        return result


    # DIAGNOSTIC
    def parse_diagnostic(self, rx, unsigned=True):
        """
        Get value in diagnostic frame.
        rx: SLAVE (1B) + FUNCTION (\x08 1B) + SUB CODE (2B) + ECHO VALUE (2B) + CRC (2B)

        :param rx: Response to diagnostic.

        :type rx: Buffer of bytes.

        :returns: Value from echo.
        :rtype: Integer/None.
        """
        if not self.check_error(rx):
            if rx[1] == DIAGNOSTIC:
                if len(rx) == 8:
                    return self.decode(rx[4:6], unsigned=unsigned)

    

    #############
    #### RAW ####
    #############

    # REGISTERS

    def raw_read_registers(self, start_address='\x00\x00', num_register=1):
        """
        Raw and parse read multiple registers.

        :param start_address: Buffer of (2) bytes with start address.
        :param num_register: Numer of registers to read.
        :param is_double: A double register occupies 4 bytes, simple 2 bytes.

        :type start_address: Buffer of bytes.
        :type num_register: Integer.
        :type is_double: Bool.

        :returns: Array with values of registers.
        :rtype: Array of integers/None.
        """
        if is_double:
            tmp_num_register = num_register*2
            register_byte = 4
        else:
            tmp_num_register = num_register
            register_byte = 2

        tx = self.read_multiple_registers(start_address , tmp_num_register, unsigned=unsigned)
        rx = self.modbus.raw(tx)

        if self.debug:
            print 'tx', list(tx)
            print 'rx', list(rx)

        if rx:
            return self.parse_read_multiple_registers(rx, register_byte, unsigned=unsigned)


    def raw_write_registers(self, start_address='\x00\x00', num_register=1, values=[], is_double=False, unsigned=True):
        """
        :param start_address: Start address to write.
        :param num_register: Numer of registers to write.
        :param values: The new values of registers.
        :param is_double: A double register occupies 4 bytes, simple 2 bytes.

        :type start_address: Buffer of (2) bytes.
        :type values: Array of integer. If is double: [0, 4294967295] ( 4 bytes when encode) else: [0, 65535] ( 2 bytes when encode).
        :type num_register: Integer.
        :type is_double: Bool.

        :returns: Number of registers affected.
        :rtype: Integer.
        """
        result = 0

        if is_double:
            tx = self.write_multiple_registers(start_address=start_address, num_register=num_register, num_byte=4, values=values, is_double=is_double, unsigned=unsigned)
        elif len(values) > 1:
            tx = self.write_multiple_registers(start_address=start_address, num_register=num_register, num_byte=2, values=values, is_double=is_double, unsigned=unsigned)
        else:
            tx = self.write_single_register(start_address, values[0], unsigned=unsigned)

        rx = self.modbus.raw(tx)

        if self.debug:
            print 'tx', list(tx)
            print 'rx', list(rx)

        if rx:
            if is_double or len(values) > 1:
                result = self.parse_write_multiple_registers(rx, unsigned)
            else:
                result = self.parse_write_single_register(rx, unsigned)

        return result


    def raw(self, tx):
        """
        Raw and parse read multiple coils.

        :param start_address: Buffer of (2) bytes with start address.
        :param num_coil: Numer of coils to read.

        :type start_address: Buffer of bytes.
        :type num_coil: Integer.

        :returns: Array with statuses of coils.
        :rtype: Array of bool/None.
        """
        tx = tx + self.modbus.get_crc(tx)
        rx = self.modbus.raw(tx)

        if self.debug:
            print 'tx', list(tx)
            print 'rx', list(rx)
        if rx:
            return rx
    #################
    ##### TO-DO #####
    #################


    ##### END TO-DO #####

if __name__ == '__main__':
    from random import randint
    import time

    import sys
    import os

    #PATH_MODBUS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/ivy_gw/modules/modbus'
    PATH_rt4all_protocol = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/ivy_gw/modules/modbus'
    sys.path.insert(0, PATH_MODBUS)

    import modbus
    f = Frame(modbus.Modbus())

    #doctest.testfile('doctest_frame.txt')
    # f = Frame(modbus.Modbus(), 1)
