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
sysPath.append( PATH_rt4all_frame  + '/RT4all_protocol/')
import time
import rt4all_protocol as protocol
import rt4all_frame as frame
import register_robot as reg

f = frame.Frame(protocol.RT4all_protocol())



from socket import *
def create_brain():
	f.raw_write_registers(reg.GO, 1)
	time.sleep(0.2)
	f.raw_write_registers(reg.GO, 0)
	s = socket(AF_INET, SOCK_STREAM)
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.bind(("", 1235))
	s.listen(1)
	conn, addr = s.accept()
	print 'Incoming connection'
	while 1:
		
		
		
		data = conn.recv(1024)
		if data == 'Goodbye':
			break
		elif data=='go':
			print 'go'
			f.raw_write_registers(reg.GO, 1)
			
		elif data == '_go':
			print '_go'			
			f.raw_write_registers(reg.GO, 0)
			
		elif data == 'back':
			print 'back'
			f.raw_write_registers(reg.BACK, 1)
		elif data == '_back':
			print '_back'
			f.raw_write_registers(reg.BACK, 0)
		
			
		
	conn.close()
	s.shutdown(2)	
	s.close()
	print 'Server shutdown.'

if __name__ == '__main__':
    create_brain()
    
