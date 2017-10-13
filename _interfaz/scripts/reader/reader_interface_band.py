"""Samples's reader."""

from __future__ import print_function
from sys import path as sysPath
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))

sysPath.append((filepath + "/../"))
import rticonnextdds_connector as rti



connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/band.xml")
inputDDS = connector.getInput("MySubscriber::MyBandReader")

for i in range(1, 500):
    inputDDS.take()
    numOfSamples = inputDDS.samples.getLength()
    for j in range(1, numOfSamples+1):
        if inputDDS.infos.isValid(j):
          

            # Or you can just access the field directly
            go = inputDDS.samples.getBoolean(j, "go")
            back = inputDDS.samples.getBoolean(j, "back")
	    band_id = inputDDS.samples.getString(j, "band_id")
            toPrint ="ID: " + repr(band_id) + " Received go: " + repr(go) + " back: " + repr(back)

            print(toPrint)
    sleep(2)
