"""Samples's reader."""

from __future__ import print_function
from sys import path as sysPath
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))

sysPath.append((filepath + "/../"))
import rticonnextdds_connector as rti



connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/robot.xml")
inputDDS = connector.getInput("MySubscriber::MyRobotReader")

for i in range(1, 500):
    inputDDS.take()
    numOfSamples = inputDDS.samples.getLength()
    for j in range(1, numOfSamples+1):
        if inputDDS.infos.isValid(j):
          

            # Or you can just access the field directly
	    cam = inputDDS.samples.getBoolean(j, "cam")
            temperature = inputDDS.samples.getNumber(j, "temperature")
            humidity = inputDDS.samples.getNumber(j, "humidity")
	    robot_id = inputDDS.samples.getNumber(j, "robot_id")
	    servo_angle_position=inputDDS.samples.getNumber(j, "servo_angle_position")
            toPrint ="Camera: " + repr(cam) + " ID: " + repr(int(robot_id)) + " Received temperature: " + repr(temperature) + " humidity: " + repr(humidity) + " servo_angle_position: " + repr(servo_angle_position)

            print(toPrint)
    sleep(2)
