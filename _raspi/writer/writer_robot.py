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
PATH_rt4all_frame = osPath.dirname(osPath.realpath(__file__))
sysPath.append( PATH_rt4all_frame  + '/../modules/RT4all_protocol/')

import rt4all_protocol as protocol
import rt4all_frame as frame
import register_robot as reg



connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/robot.xml")
outputDDS = connector.getOutput("MyPublisher::MyRobotWriter")
equipo = socket.gethostname()

f = frame.Frame(protocol.RT4all_protocol())
vector = f.raw_read_registers(reg.temperature,3)
while True:
	vector = f.raw_read_registers(reg.temperature,3)
	if vector is not None:
		if len(vector) == 3:
			outputDDS.instance.setNumber("cam", 1)
			outputDDS.instance.setNumber("temperature", vector[0])
			outputDDS.instance.setNumber("humidity", vector[1])
			outputDDS.instance.setNumber("robot_id", 1)
			outputDDS.instance.setNumber("servo_angle_position", vector[2])
			outputDDS.write()
	sleep(2)
