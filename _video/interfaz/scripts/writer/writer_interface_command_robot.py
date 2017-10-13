"""Robot's writer."""

from sys import path as sysPath
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../")
import rticonnextdds_connector as rti
import socket
import fcntl
import struct
import sys

connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/action_robot.xml")
outputDDS = connector.getOutput("MyPublisher::MyActionRobotWriter")

actions = dict.fromkeys(["go", "back", "left", "right","scoop","cam_l","cam_r"], 0)

"""for line in sys.stdin:
	accion = line[:-1]

if actions.get(accion) != None:
	actions[accion] = 1;"""

for i in range(1, 5):
	outputDDS.instance.setBoolean("go", 1)
	outputDDS.instance.setBoolean("back", actions["back"])
	outputDDS.instance.setBoolean("left", 1)
	outputDDS.instance.setBoolean("right", actions["right"])
	outputDDS.instance.setBoolean("scoop", actions["scoop"])
	outputDDS.instance.setBoolean("cam_l", actions["cam_l"])
	outputDDS.instance.setBoolean("cam_r", actions["cam_r"])

	outputDDS.write()
	sleep(0.2)