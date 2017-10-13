#! /usr/bin/env python

"""
Handler General Purpose Input/Output (GPIO)
GPIO 24 Channel pin
GPIO 23 Transfer and receive pin

Average enable tx/rx is 0.00000369240 seg.
"""

__author__ = 'Javi Ortega'
__copyright__ = 'Copyright (C) 2017'
__license__ = 'MIT (expat) License'
__version__ = '0.1'
__maintainer__ = 'Javi Ortega'
__email__ = 'javier.ortega@whitewallenergy.com'


import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gpio import gpio

GPIO_EN = 24    #: Channel pin
GPIO_TR = 23    #: Transfer and receive pin

class Rs485:
    """"""
    def __init__(self):
        """"""
        self.gpio = gpio.Gpio()
        self.gpio.setup()

        self.gpio.output(GPIO_EN)
        self.gpio.clear(GPIO_EN)

        self.gpio.output(GPIO_TR)
        self.gpio.clear(GPIO_TR)

        self.gpio.set(GPIO_EN)

    def set_tx_enable(self):
        """
        Set GPIO 23 to transfer (GPIO 23 = 1)

        :returns: GPIO Address, 0 to error
        :rtype: integer
        """
        return self.gpio.set(GPIO_TR)

    def set_rx_enable(self):
        """
        Set GPIO 23 to receive (GPIO 23 = 0)

        :returns: GPIO Address, 0 to error
        :rtype: integer
        """
        return self.gpio.clear(GPIO_TR)

    def is_tx_enable(self):
        """
        Return transfer status

        :returns: GPIO 23 != 0
        :rtype: boolean
        """
        return self.gpio.read(GPIO_TR) != 0

    def is_rx_enable(self):
        """
        Return receive status

        :returns: GPIO 23 == 0
        :rtype: boolean
        """
        return self.gpio.read(GPIO_TR) == 0

if __name__ == "__main__":
    c = Rs485()
    print 'is_writing', c.is_tx_enable()
    print 'is_written', c.is_rx_enable()

    print c.set_tx_enable()
    print 'writing...'
    print 'is_writing', c.is_tx_enable()
    print 'is_written', c.is_rx_enable()

    print c.set_rx_enable()
    print '...written'
    print 'is_writing', c.is_tx_enable()
    print 'is_written', c.is_rx_enable()
