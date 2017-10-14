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
                          filepath + "/../XML/robot.xml")
outputDDS = connector.getOutput("MyPublisher::MyRobotWriter")
equipo = socket.gethostname()
print equipo

for i in range(1, 500):
    outputDDS.instance.setNumber("cam", 0)
    outputDDS.instance.setNumber("temperature", 16)
    outputDDS.instance.setNumber("humidity", 67)
    outputDDS.instance.setNumber("robot_id", 1)
    outputDDS.instance.setNumber("servo_angle_position", 34)
    outputDDS.write()
    sleep(1)
