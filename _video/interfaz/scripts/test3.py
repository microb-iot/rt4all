import sys, json

# Read from electron the key pressed
for line in sys.stdin:
	print line[:-1]

# TODO: Send data here

sys.exit()