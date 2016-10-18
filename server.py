#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socketserver
import sys
import json


class SIPRegisterHandler(socketserver.DatagramRequestHandler):

    client_list = []
    
    def handle(self):        
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n") 

        line = self.rfile.read()
        data = line.decode('utf-8')
        chops = data.split(' ')
        if chops[0] == 'REGISTER':
            self.client_list.append([chops[1][4:],
                                    {"address": self.client_address[0],
                                     "expires": chops[4][:-4]}])
            if chops[3][2:-1] == 'Expires':
                if chops[4][:-4] == '0':
                    pass #Buscar como eliminar elementos de una lista        
            
        print("El cliente nos manda:" + '\r\n' + data)
        print('IP: ', self.client_address[0])
        print('Puerto: ', self.client_address[1])
        print('Los clientes existentes son:', self.client_list)
        
        self.register2json()
        
    def register2json(self):
        json_file = open('registered.json', 'w')
        json.dump(self.client_list, json_file)
        
if __name__ == "__main__":

    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Finalizado servidor")   
