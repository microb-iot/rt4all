"""Samples's reader."""

from __future__ import print_function
from sys import path as sysPath
from os import path as osPath
from time import sleep
import json, ast, sys
filepath = osPath.dirname(osPath.realpath(__file__))

sysPath.append((filepath + "/../"))
import rticonnextdds_connector as rti


def createTXT(file, data):
    myfile = open("../../report/"+file, 'a')
    myfile.write(str(data)+", ")
    myfile.close()


connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/robot.xml")
inputDDS = connector.getInput("MySubscriber::MyRobotReader")

for i in range(1, 500):
    inputDDS.take()
    numOfSamples = inputDDS.samples.getLength()
    for j in range(1, numOfSamples+1):
        if inputDDS.infos.isValid(j):
          
            sample = inputDDS.samples.getDictionary(j)

            """cam = inputDDS.samples.getBoolean(j, "cam")
            temperature = inputDDS.samples.getNumber(j, "temperature")
            humidity = inputDDS.samples.getNumber(j, "humidity")
            robot_id = inputDDS.samples.getNumber(j, "robot_id")
            servo_angle_position=inputDDS.samples.getNumber(j, "servo_angle_position")"""
            salida = ast.literal_eval(json.dumps(sample))
            print(salida)

            createTXT("robotTemperature_"+str(robot_id)+".txt", temperature)
            createTXT("robotHumidity_"+str(robot_id)+".txt", humidity)
            createTXT("robotServoAngle"+str(robot_id)+".txt", servo_angle_position)

    sleep(2)

sys.exit()




