
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
machine_ip=get_ip_address('wlp2s0b1')
print machine_ip
for i in range(1, 500):
    outputDDS.instance.setString("machine", "Shovel")
    outputDDS.instance.setNumber("machine_id", 1)
    outputDDS.instance.setString("machine_ip", '192.168.1.199')
    outputDDS.write()
    sleep(1)
