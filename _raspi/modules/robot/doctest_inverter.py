#! /usr/bin/env python
"""
Test comunication
"""

__author__ = 'Juan Carlos Chaves'
__copyright__ = 'Copyright (C) 2017'
__license__ = 'MIT (expat) License'
__version__ = '0.1'
__maintainer__ = 'Juan Carlos Chaves'
__email__ = 'juan.chaves@whitewallenergy.com'

import struct
from frame import Frame
import mx2
import doctest


import sys
import os

#PATH_MODBUS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/ivy_gw/modules/modbus'
PATH_MODBUS = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/ivy_gw/modules/modbus'
sys.path.insert(0, PATH_MODBUS)

import modbus

"""
TO-DO
Hay forma de parametrizar esto para que funcione en big y little endian ??

"""


class TestFrame:
    """"""
    def __init__(self, modbus, slave_address=mx2.DEFAULT_SLAVE_ADDRESS, big_endian=mx2.DEFAULT_BIG_ENDIAND):
        self.modbus = modbus
        self.frame = Frame(self.modbus, slave_address, big_endian)

        self.three_phase = mx2.DEFAULT_IS_THREE_PHASE
        self.height_impulse = mx2.DEFAULT_HEIGHT_IMPULSE # meters
        self.water_density = mx2.DEFAULT_DENSITY    # kg/m^3
        self.max_power = mx2.DEFAULT_MAX_POWER        # Watts
        self.flow_at_maximum_power = mx2.DEFAULT_FLOW_AT_MAXIMUM_POWER   # m^3/h

    """ CLASS METHODS """

    def read_coil(self):
        """
        It will only be correct if the run command is disabled
        >>> i.read_coil()
        tx ['\\x01', '\\x01', '\\x00', '\\x12', '\\x00', '\\x01', ']', '\\xcf']
        rx ['\\x01', '\\x01', '\\x01', '\\x00', 'Q', '\\x88']
        [False]
        """
        return self.frame.raw_read_coils(start_address=mx2.COIL_RUN, num_coil=1)

    def actualize_coil(self):
        """
        Try actualize the value of a coil
        >>> i.actualize_coil()
        tx ['\\x01', '\\x05', '\\x00', '\\x00', '\\x00', '\\x00', '\\xcd', '\\xca']
        rx ['\\x01', '\\x05', '\\x00', '\\x00', '\\x00', '\\x00', '\\xcd', '\\xca']
        1
        """
        return self.frame.raw_write_coils(start_address=mx2.COIL_SET_RUN, num_coil=1 , num_byte=1,statuses=[False])

    def actualize_coils(self):
        """
        Try changing the values of a coils
        >>> i.actualize_coils()
        tx ['\\x01', '\\x0f', '\\x00', '\\x06', '\\x00', '\\x04', '\\x02', '\\x0c', '\\x00', '\\xe2', '\\xb6']
        rx ['\\x01', '\\x0f', '\\x00', '\\x06', '\\x00', '\\x04', '\\xb4', '\\t']
        0
        """
        return self.frame.raw_write_coils(start_address=mx2.COIL_SE1, num_coil=4 , num_byte=2,statuses=[False,False, True, True])

    def actualize_one_register(self):
        """
        Send the command to actualize the value of a register
        >>> i.actualize_one_register()
        tx ['\\x01', '\\x06', '\\x16', '$', '\\x00', ' ', '\\xcc', 'Q']
        rx ['\\x01', '\\x06', '\\x16', '$', '\\x00', ' ', '\\xcc', 'Q']
        1
        """
        return self.frame.raw_write_registers(start_address=mx2.P037, num_register=1, values=[32], is_double=False, unsigned=True)

    def read_one_register(self):
        """
        Send the command to read the value of a register
        >>> i.read_one_register()
        tx ['\\x01', '\\x03', '\\x16', '$', '\\x00', '\\x01', '\\xc0', 'I']
        rx ['\\x01', '\\x03', '\\x02', '\\x00', ' ', '\\xb9', '\\x9c']
        [32]
        """
        return self.frame.raw_read_registers(start_address=mx2.P037, num_register=1, is_double=False)


    def actualize_two_register(self):
        """
        Send the command to actualize the values of two registers
        >>> i.actualize_two_register()
        tx ['\\x01', '\\x10', '\\x16', '$', '\\x00', '\\x02', '\\x04', '\\x00', ' ', '\\x00', '\\x01', '\\xd6', '.']
        rx ['\\x01', '\\x10', '\\x16', '$', '\\x00', '\\x02', '\\x05', '\\x8b']
        2
        """
        return self.frame.raw_write_registers(start_address=mx2.P037, num_register=2, values=[32,1], is_double=False, unsigned=True)

    def read_two_register(self):
        """
        Send the command to read the values of two registers
        >>> i.read_two_register()
        tx ['\\x01', '\\x03', '\\x16', '$', '\\x00', '\\x02', '\\x80', 'H']
        rx ['\\x01', '\\x03', '\\x04', '\\x00', ' ', '\\x00', '\\x01', ':', '9']
        [32, 1]
        """
        return self.frame.raw_read_registers(start_address=mx2.P037, num_register=2, is_double=False)


    def actualize_one_register_double(self):
        """
        Send the command to actualize the values of a register(2 bytes)
        >>> i.actualize_one_register_double()
        tx ['\\x01', '\\x10', '\\x12', 'N', '\\x00', '\\x02', '\\x04', '\\x00', '\\x00', '\\x01', '\\x00', '\\xa3', '#']
        rx ['\\x01', '\\x10', '\\x12', 'N', '\\x00', '\\x02', '$', '\\xa7']
        2
        """
        return self.frame.raw_write_registers(start_address=mx2.A061, num_register=1, values=[256], is_double=True, unsigned=True)

    def read_one_register_double(self):
        """
        Send the command to read the value of a register(2 bytes)
        >>> i.read_one_register_double()
        tx ['\\x01', '\\x03', '\\x12', 'N', '\\x00', '\\x02', '\\xa1', 'd']
        rx ['\\x01', '\\x03', '\\x04', '\\x00', '\\x00', '\\x01', '\\x00', '\\xfb', '\\xa3']
        [256]
        """
        return self.frame.raw_read_registers(start_address=mx2.A061, num_register=1, is_double=True)


    def actualize_two_register_double(self):
        """
        Send the command to actualize the values of two registers(2 bytes)
        >>> i.actualize_two_register_double()
        tx ['\\x01', '\\x10', '\\x12', 'N', '\\x00', '\\x04', '\\x08', '\\x00', '\\x00', '\\x01', '\\x00', '\\x00', '\\x00', '\\x00', '\\xfa', '\\xe6', '\\xd2']
        rx ['\\x01', '\\x10', '\\x12', 'N', '\\x00', '\\x04', '\\xa4', '\\xa5']
        4
        """
        return self.frame.raw_write_registers(start_address=mx2.A061, num_register=2, values=[256,250], is_double=True, unsigned=True)



    def read_two_register_double(self):
        """
        Send the command to read the value of two registers(2 bytes)
        >>> i.read_two_register_double()
        tx ['\\x01', '\\x03', '\\x12', 'N', '\\x00', '\\x04', '!', 'f']
        rx ['\\x01', '\\x03', '\\x08', '\\x00', '\\x00', '\\x01', '\\x00', '\\x00', '\\x00', '\\x00', '\\xfa', '\\x14', 'E']
        [256, 250]
        """
        return self.frame.raw_read_registers(start_address=mx2.A061, num_register=2, is_double=True)

    def actualize_one_register_signed(self):
        """
        Send the command to actualize the value of a register
        >>> i.actualize_one_register_signed()
        tx ['\\x01', '\\x06', '\\x16', ':', '\\xff', '\\xff', '\\xac', '?']
        rx ['\\x01', '\\x06', '\\x16', ':', '\\xff', '\\xff', '\\xac', '?']
        1
        """
        return self.frame.raw_write_registers(start_address=mx2.P057, num_register=1, values=[-1], is_double=False, unsigned=False)

    def read_one_register_signed(self):
        """
        Send the command to read the value of a register
        >>> i.read_one_register_signed()
        tx ['\\x01', '\\x03', '\\x16', ':', '\\x00', '\\x01', '\\xa0', 'O']
        rx ['\\x01', '\\x03', '\\x02', '\\xff', '\\xff', '\\xb9', '\\xf4']
        [-1]
        """

        return self.frame.raw_read_registers(start_address=mx2.P057, num_register=1, is_double=False, unsigned=False)

    def actualize_two_register_signed(self):
        """
        TO-DO no encuentro dos registros simples con signo que sean consecutivos
        Send the command to actualize the values of two registers
        >>> i.actualize_two_register_signed()
        tx ['\\x01', '\\x10', '\\x16', '$', '\\x00', '\\x02', '\\x04', '\\x00', ' ', '\\x00', '\\x01', '\\xd6', '.']
        rx ['\\x01', '\\x10', '\\x16', '$', '\\x00', '\\x02', '\\x05', '\\x8b']
        2
        """
        return self.frame.raw_write_registers(start_address=mx2.P037, num_register=2, values=[32,1], is_double=False, unsigned=True)

    def read_two_register_signed(self):
        """
        TO-DO no encuentro dos registros simples con signo que sean consecutivos
        Send the command to read the values of two registers
        >>> i.read_two_register()
        tx ['\\x01', '\\x03', '\\x16', '$', '\\x00', '\\x02', '\\x80', 'H']
        rx ['\\x01', '\\x03', '\\x04', '\\x00', ' ', '\\x00', '\\x01', ':', '9']
        [32, 1]
        """
        print self.frame.raw_read_registers(start_address=mx2.P037, num_register=2, is_double=False)


    def actualize_one_register_double_signed(self):
        """
        Send the command to actualize the values of a signed register(2 bytes)
        >>> i.actualize_one_register_double_signed()
        tx ['\\x01', '\\x10', '\\x16', '=', '\\x00', '\\x02', '\\x04', '\\xff', '\\xff', '\\xff', '8', '\\x97', 'D']
        rx ['\\x01', '\\x10', '\\x16', '=', '\\x00', '\\x02', '\\xd4', 'L']
        2
        """
        return self.frame.raw_write_registers(start_address=mx2.P060, num_register=1, values=[-200], is_double=True, unsigned=False)

    def read_one_register_double_signed(self):
        """
        Send the command to read the value of a register(2 bytes)
        >>> i.read_one_register_double_signed()
        tx ['\\x01', '\\x03', '\\x16', '=', '\\x00', '\\x02', 'Q', '\\x8f']
        rx ['\\x01', '\\x03', '\\x04', '\\xff', '\\xff', '\\xff', '8', '\\xba', '5']
        [-200]
        """
        return self.frame.raw_read_registers(start_address=mx2.P060, num_register=1, is_double=True, unsigned=False)


    def actualize_two_register_double_signed(self):
        """
        Send the command to actualize the values of two registers(2 bytes)
        >>> i.actualize_two_register_double_signed()
        tx ['\\x01', '\\x10', '\\x16', '=', '\\x00', '\\x04', '\\x08', '\\xff', '\\xff', '\\xff', '8', '\\xff', '\\xfc', '-', 'E', '\\xf5', '\\xf9']
        rx ['\\x01', '\\x10', '\\x16', '=', '\\x00', '\\x04', 'T', 'N']
        4
        """
        return self.frame.raw_write_registers(start_address=mx2.P060, num_register=2, values=[-200,-250555], is_double=True, unsigned=False)



    def read_two_register_double_signed(self):
        """
        Send the command to read the value of two registers(2 bytes)
        >>> i.read_two_register_double_signed()
        tx ['\\x01', '\\x03', '\\x16', '=', '\\x00', '\\x04', '\\xd1', '\\x8d']
        rx ['\\x01', '\\x03', '\\x08', '\\xff', '\\xff', '\\xff', '8', '\\xff', '\\xfc', '-', 'E', 'L', '\\x91']
        [-200, -250555]
    """
        return self.frame.raw_read_registers(start_address=mx2.P060, num_register=2, is_double=True, unsigned=False)



if __name__ == '__main__':
    i = TestFrame(modbus.Modbus())
    doctest.testmod()
