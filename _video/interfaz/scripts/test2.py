import sys
import time

i = 0
j = 0
while j < 200:
	print i + 0.5
	if i > 100: i = 0
	i = i+1
	j = j+1
	#Poner en el caso de ejecutar el script sin -u
	#sys.stdout.flush()
	time.sleep(0.5)

sys.exit()