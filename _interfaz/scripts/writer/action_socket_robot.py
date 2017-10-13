#!/usr/bin/env python
 
import sys
#importamos el modulo para trabajar con sockets
import socket
 
#Creamos un objeto socket para el servidor. Podemos dejarlo sin parametros pero si 
#quieren pueden pasarlos de la manera server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
 
#Nos conectamos al servidor con el metodo connect. Tiene dos parametros
#El primero es la IP del servidor y el segundo el puerto de conexion
s.connect(("192.168.1.137", 9999))
 
#Creamos un bucle para retener la conexion
"""while True:
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    for line in sys.stdin:
		mensaje = line[:-1]
 
    #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
    
 
    #Si por alguna razon el mensaje es close cerramos la conexion
    if mensaje == "close":
        break"""

"""for line in sys.stdin:
	mensaje = line[:-1]
	s.send(mensaje)"""

line=' '
while line:
    line = sys.stdin.readline()
    s.send(line)
    sys.stdout.flush()

 
#Imprimimos la palabra Adios para cuando se cierre la conexion
print "Adios."
 
#Cerramos la instancia del objeto servidor
s.close()
