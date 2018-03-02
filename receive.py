import socket
import serial
import RPi.GPIO as GPIO
import time

#UDP_IP = "128.119.82.231"
UDP_IP = "169.254.68.246"
#UDP_PORT = 5005
UDP_PORT = 4800

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ser = serial.Serial('/dev/ttyS0',9600)

sock.bind((UDP_IP, UDP_PORT))
#sock.listen(5)

while True:
    try:
	data, addr = sock.recvfrom(1024)
	ser.write(data)
	print(data)
    except socket.error, e:
        print "socket error ", e
        sock.close()
        break
