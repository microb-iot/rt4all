"""Samples's reader."""

from __future__ import print_function
from sys import path as sysPath
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))

sysPath.append((filepath + "/../"))
import rticonnextdds_connector as rti



connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/action_robot.xml")
inputDDS = connector.getInput("MySubscriber::MyActionRobotReader")

while True:
	
	inputDDS.take()
	numOfSamples = inputDDS.samples.getLength()
	for j in range(1, numOfSamples+1):
		if inputDDS.infos.isValid(j):
			go = inputDDS.samples.getBoolean(j, "go")
			back = inputDDS.samples.getBoolean(j, "back")
			left = inputDDS.samples.getBoolean(j, "left")
			right = inputDDS.samples.getBoolean(j, "right")
			scoop = inputDDS.samples.getBoolean(j, "scoop")
			cam_l = inputDDS.samples.getBoolean(j, "cam_l")
			cam_r = inputDDS.samples.getBoolean(j, "cam_r")
			
			toPrint = "avanza: " + repr(go) + repr(back) + repr(left) + "samples: " + repr(numOfSamples)

			print(toPrint)
	sleep(0.3)
