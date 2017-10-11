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

def get_ip_address(ifname):
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])



connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/machine.xml")
outputDDS = connector.getOutput("MyPublisher::MyMachineWriter")
equipo = socket.gethostname()
print equipo
machine_ip=get_ip_address('enp0s3')
print machine_ip
for i in range(1, 500):
    outputDDS.instance.setString("machine", "robot")
    outputDDS.instance.setNumber("machine_id", 0)
    outputDDS.instance.setString("machine_ip", machine_ip)
    outputDDS.write()
    sleep(1)
