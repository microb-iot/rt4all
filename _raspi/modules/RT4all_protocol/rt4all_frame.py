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
import register_robot

# REGISTERS
READ_MULTIPLE_REGISTERS = '\x03'
WRITE_SINGLE_REGISTER = '\x06'





class Frame:
	""""""
	def __init__(self, protocol, slave_address=1):
		""""""
		self.debug = True
		self.protocol = protocol
		self.slave_address = self.encode(slave_address, 1)

	def create_frame(self, code_func='\x00', start_address='\x00\x00', data=''):
		"""
		Return frame: slave_address + code_func + start_address + data 

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

	def decode(self, hexadecimal='\x00\x00', num_byte=2):
		"""
		Decode hexadecimal value to integer value.

		:param hexadecimal: Buffer of bytes to decode.
		:param num_byte: Numer of byte to decode.

		:type hexadecimal: Buffer of bytes.
		:type num_byte: Integer.

		:returns: Decoded value.
		:rtype: Integer.
		"""
		return struct.unpack(self.get_format(num_byte), hexadecimal)[0]

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


		fmt = '>' 

		if num_byte == 1:
			fmt += 'B' 
		elif num_byte == 2:
			fmt += 'H'
		elif num_byte == 4:
			fmt += 'I'

		return fmt

    ##########
    # FRAMES #
    ##########

    # REGISTERS
	def read_multiple_registers(self, start_address='\x00\x00', num_register=1):
		"""
		Creates a frame to read multiple registers.

		:param start_address: Start address to read.
		:param num_register: Number of registers (max 16).

		:type start_address: Buffer of (2) bytes.
		:type num_register: Integer [1, 16] ( 2 bytes when encode).

		:returns: Frame to read multiple registers.
		:rtype: Buffer of bytes.
		
		"""
		
		return self.create_frame(READ_MULTIPLE_REGISTERS, start_address, self.encode(num_register))

	def write_single_register(self, start_address='\x00\x00', value=1):
		"""
		Creates a frame to write single register.

		:param start_address: Start address to write.
		:param value: The new value of register.

		:type start_address: Buffer of (2) bytes.
		:type value: Integer [0, 65535] ( 2 bytes when encode).

		:returns: Frame to write single register.
		:rtype: Buffer of bytes.
		"""
		
		return self.create_frame(WRITE_SINGLE_REGISTER, start_address, self.encode(value))

   

    

    ###################
    ##### PARSING #####
    ###################

    # REGISTERS
	def parse_read_multiple_registers(self, rx, register_byte=2):
		"""
		Translate response frame read multiple registers to array of integers.
		rx: SLAVE (1B) + FUNCTION (\x03 1B) + BYTE DATA (1B) + DATA ([2, 32] B) 

		:param rx: Response to read multiple registers.
		:param register_byte: Number of byte for each register.

		:type rx: Buffer of bytes.
		:type register_byte: Integer.

		:returns: Array with values of registers.
		:rtype: Array of integers.
		"""
		result = []

		
		if rx[1] == READ_MULTIPLE_REGISTERS:
			len_rx = len(rx)
			if len_rx >= 7 or len_rx <= 37:
				for v in [rx[i:i+register_byte] for i in range(3, len(rx), register_byte)]:
					result.append(self.decode(v, register_byte))

	
		return result


	def parse_write_single_register(self, rx, unsigned=True):
		"""
		Translate response frame write single registers to integer.
		rx: SLAVE (1B) + FUNCTION (\x06 1B) + START ADDRESS (2B) + DATA (2B) 

		:param rx: Response to write single register.

		:type rx: Buffer of bytes.

		:returns: Number of registers affected.
		:rtype: Integer.
		"""
		result = 0
    
		if rx[1] == WRITE_SINGLE_REGISTER:
			if len(rx) == 6:
				#return self.decode(rx[4:6])
				result = 1
		return result



    

    #############
    #### RAW ####
    #############

    # REGISTERS

	def raw_read_registers(self, start_address='\x00\x00', num_register=1):
		"""
		Raw and parse read multiple registers.

		:param start_address: Buffer of (2) bytes with start address.
		:param num_register: Numer of registers to read.

		:type start_address: Buffer of bytes.
		:type num_register: Integer.

		:returns: Array with values of registers.
		:rtype: Array of integers/None.
		"""
		
		
	
		register_byte = 2

		tx = self.read_multiple_registers(start_address , num_register)
		rx = self.protocol.raw(tx)

		if self.debug:
			print 'tx', list(tx)
			print 'rx', list(rx)

		if rx:
			return self.parse_read_multiple_registers(rx, register_byte)


	def raw_write_registers(self, start_address='\x00\x00', value=0):
		"""
		:param start_address: Start address to write.
		:param value: The new value of registers.

		:type start_address: Buffer of (2) bytes.
		:type value: integer.
	.
		:returns: Number of registers affected.
		:rtype: Integer.
		"""
		result = 0

		tx = self.write_single_register(start_address, value=value)

		rx = self.protocol.raw(tx)

		if self.debug:
			print 'tx', list(tx)
			print 'rx', list(rx)

		if rx:
			result = self.parse_write_single_register(rx)

		return result


	def raw(self, tx):

		rx = self.protocol.raw(tx)

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

	PATH_rt4all_protocol = os.path.abspath(__file__) + '/rt4all_protocol'
    
	sys.path.insert(0, PATH_rt4all_protocol)

	import rt4all_protocol
	f = Frame(rt4all_protocol.RT4all_protocol())
	f.raw_write_registers(register_robot.temperature,512)
	f.raw_read_registers(register_robot.temperature,2)

	
	
