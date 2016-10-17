#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import sys


SERVER = str(sys.argv[1])
PORT = int(sys.argv[2])
line = str(' '.join(sys.argv[3:]))

chops = line.split(' ')
if sys.argv[3] == 'register':
        line = str(chops[0].upper() + ' sip: ' + chops[1])

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", line)
    my_socket.send(bytes(line, 'utf-8') + b' SIP/2.0\r\n\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
