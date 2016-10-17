#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler): #clase para manejar peticiones
    """
    Echo server class
    """
#hereda de DatagramRequestHandler del modulo socketserver
#no tiene init ya que lo hereda de la clase padre

    def handle(self):        
        self.wfile.write(b"Hemos recibido tu peticion") 
        #wfile y rfile son atributos que abstraen del socket como si fuera un fichero
        for line in self.rfile: 
        #rfile va iterando sobre las lineas como si fuera un fichero de lectura
        #podemos ir escribiendo en el con wfile.write()
            print("El cliente nos manda: ", line.decode('utf-8')) #envia secuencias de bytes
            print('IP: ', self.client_address[0])
            print('Puerto: ', self.client_address[1])

if __name__ == "__main__":

    serv = socketserver.UDPServer(('', int(sys.argv[1])), EchoHandler) #se instancia la clase EchoHandler indicando IP y puerto donde el servidor escucha
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor") #finaliza escucha con Ctrl+C
        
