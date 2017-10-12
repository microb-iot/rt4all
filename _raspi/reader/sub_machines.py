##############################################################################
# Copyright (c) 2005-2015 Real-Time Innovations, Inc. All rights reserved.
# Permission to modify and use for internal purposes granted.
# This software is provided "as is", without warranty, express or implied.
##############################################################################
"""Samples's reader."""

from __future__ import print_function
from sys import path as sysPath
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append((filepath + "/../"))

import rticonnextdds_connector as rti



connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/machine.xml")
inputDDS = connector.getInput("MySubscriber::MyMachineReader")

for i in range(1, 500):
    inputDDS.take()
    numOfSamples = inputDDS.samples.getLength()
    for j in range(1, numOfSamples+1):
        if inputDDS.infos.isValid(j):

            # Or you can just access the field directly
            machine = inputDDS.samples.getString(j, "machine")
            machine_id = inputDDS.samples.getNumber(j, "machine_id")
	    machine_ip = inputDDS.samples.getString(j, "machine_ip")
            toPrint = "Machine: " + repr(machine) + " ID: " + repr(machine_id) + \
                      " IP: " + repr(machine_ip) 

            # This gives you a dictionary
            """sample = inputDDS.samples.getDictionary(j)
            x = sample['x']
            y = sample['y']"""

            # Or you can just access the field directly
            name = inputDDS.samples.getString(j, "machine")
            machine_id = inputDDS.samples.getNumber(j, "machine_id")
            machine_ip = inputDDS.samples.getString(j, "machine_ip")
            toPrint = "Name: " + name + " Id: " + repr(machine_id) + " Ip: " + machine_ip 


            print(toPrint)
    sleep(1)
