##############################################################################
# Copyright (c) 2005-2015 Real-Time Innovations, Inc. All rights reserved.
# Permission to modify and use for internal purposes granted.
# This software is provided "as is", without warranty, express or implied.
##############################################################################
"""Samples's writer."""

from sys import path as sysPath
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../")
import rticonnextdds_connector as rti
import socket
import fcntl
import struct



connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/band.xml")
outputDDS = connector.getOutput("MyPublisher::MyBandWriter")
equipo = socket.gethostname()
print equipo

for i in range(1, 500):
    outputDDS.instance.setBoolean("go", 0)
    outputDDS.instance.setBoolean("back", 1)
    outputDDS.instance.setNumber("band_id", 0)
    outputDDS.write()
    sleep(1)
