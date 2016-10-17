#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
SERVER = str(sys.argv[1])
PORT = int(sys.argv[2])
LINE = str(' '.join(sys.argv[3:]))



# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT)) #conecta al servidor 
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n') #b convierte a bytes, r y n son el salto de linea y la sangria
    data = my_socket.recv(1024) #1024 -- valor del buffer en bytes
    print('Recibido -- ', data.decode('utf-8'))
# al terminar el with la conexion se cierra automaticamente

print("Socket terminado.")
