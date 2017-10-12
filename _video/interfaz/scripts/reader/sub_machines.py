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
import json, ast, sys
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append((filepath + "/../"))

import rticonnextdds_connector as rti



connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/machine.xml")
inputDDS = connector.getInput("MySubscriber::MyMachineReader")

for i in range(1, 5):
    inputDDS.take()
    numOfSamples = inputDDS.samples.getLength()
    for j in range(1, numOfSamples+1):
        if inputDDS.infos.isValid(j):

            # This gives you a dictionary
            sample = inputDDS.samples.getDictionary(j)
            #Para eliminar las 'u' (unicode), del diccionario
            salida = ast.literal_eval(json.dumps(sample))
            print(salida)
    sleep(1)

sys.exit()
