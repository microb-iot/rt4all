from sys import path as sysPath
from os import path as osPath
from time import sleep
import rt4all_protocol
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../")
import rticonnextdds_connector as rti
import socket
import fcntl
import struct

m = rt4all_protocol.RT4all_protocol()


from socket import *
def create_brain():
	s = socket(AF_INET, SOCK_STREAM)
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.bind(("", 1234))
	s.listen(1)
	conn, addr = s.accept()
	print 'Incoming connection'
	while 1:
		
		
		
		data = conn.recv(1024)
		if data == 'Goodbye':
			break
		elif data=='go':
			print 'go'
			tx = '\x01\x06\x00\x08\x00\x01'
			rx = m.raw(tx)
		elif data == '_go':
			print '_go'			
			tx = '\x01\x06\x00\x08\x00\x00'
			rx = m.raw(tx)
		elif data == 'back':
			print 'back'
		elif data == '_back':
			print '_back'
		elif data == 'left':
			print 'left'
		elif data == '_left':
			print '_left'
		elif data == 'right':
			print 'right'
		elif data == '_right':
			print '_right'
			
		
	conn.close()
	s.shutdown(2)	
	s.close()
	print 'Server shutdown.'

if __name__ == '__main__':
    create_brain()
    
