#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socketserver
import sys
import json
import time


class SIPRegisterHandler(socketserver.DatagramRequestHandler):

    client_list = []
    
    def handle(self):        
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n") 

        line = self.rfile.read()
        data = line.decode('utf-8')
        chops = data.split(' ')
        hora = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))
        
        if chops[0] == 'REGISTER':
            client = [chops[1][4:],
                     {"address": self.client_address[0],
                      "expires": str(hora) + ' +' + chops[3][:-4]}]
            self.client_list.append(client)
            print(chops[2][8:-1])
            if chops[2][9:-1] == 'Expires':
                if chops[3][:-4] == '0':
                    self.client_list.remove(client)        
            
        print("El cliente nos manda:" + '\r\n' + data)
        print('IP: ', self.client_address[0])
        print('Puerto: ', self.client_address[1])
        print('Los clientes existentes son:', self.client_list)
        
        self.register2json()
        
    def register2json(self):
        json_file = open('registered.json', 'w')
        json.dump(self.client_list, json_file, indent = '\t')
        
if __name__ == "__main__":

    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Finalizado servidor")   
