#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import sys

try:
    SERVER = str(sys.argv[1])
    PORT = int(sys.argv[2])
    line = str(' '.join(sys.argv[3:5]))
    expires_value = sys.argv[5]
except:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value.")

chops = line.split(' ')
sip_str = ' SIP/2.0\r\n'
expires_str = 'Expires: ' + expires_value + '\r\n\r\n'
if sys.argv[3] == 'register':
        line = str(chops[0].upper() + ' sip:' + chops[1] + sip_str + expires_str)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:" + '\r\n' + line)
    my_socket.send(bytes(line, 'utf-8'))
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
