#! /usr/bin/env python

"""
Handler General Purpose Input/Output (GPIO)
"""

__author__ = 'XXX'
__copyright__ = 'Copyright (C) 2016'
__email__ = 'info@whitewallenergy.com'

import os
import platform
import ctypes

FILE_LIB = 'gpio.so'
FILE_LIB_DUMMY = 'dummy.so'
FOLDER_LIB = 'lib'

PATH_CURRENT = os.path.dirname(os.path.abspath(__file__))
PATH_LIB = os.path.join(PATH_CURRENT, FOLDER_LIB)

PLATFORM_MIPS = 'mips' == platform.machine()

PATH_GPIO = os.path.join(PATH_LIB, FILE_LIB) if PLATFORM_MIPS else os.path.join(PATH_LIB, FILE_LIB_DUMMY)

class Gpio():
    """"""
    def __init__(self):
        """"""
        self.lib = ctypes.cdll.LoadLibrary(PATH_GPIO)

    def setup(self):
        """
        Setup address map

        :returns: Status setup: -1 Open failed '/dev/mem', -2 Map failed, 0 Map success
        :rtype: integer
        """
        return self.lib.gpio_setup()

    def get_dir(self, gpio):
        """
        Return gpio address

        :param gpio: Number of gpio
        :type gpio: integer

        :returns: Direction
        :rtype: integer
        """
        return self.lib.gpio_get_dir(gpio)

    def output(self, gpio):
        """
        Enable pin and set value out

        :param gpio: Number of gpio
        :type gpio: integer
        """
        self.lib.gpio_output(gpio)

    def input(self, gpio):
        """
        Enable pin and set value in

        :param gpio: Number of gpio
        :type gpio: integer
        """
        self.lib.gpio_input(gpio)

    def read(self, gpio):
        """
        :param gpio: Number of gpio
        :type gpio: integer

        :returns: Get gpio value
        :rtype: integer
        """
        return self.lib.gpio_read(gpio)

    def set(self, gpio):
        """
        Set gpio value 1

        :param gpio: Number of gpio
        :type gpio: integer
        """
        self.lib.gpio_set(gpio)

    def clear(self, gpio):
        """
        Set gpio value 0

        :param gpio: Number of gpio
        :type gpio: integer
        """
        self.lib.gpio_clear(gpio)


if __name__ == '__main__':
    g = Gpio()

    print 'Setup =>', g.setup()
    print 'PATH_GPIO', PATH_GPIO
