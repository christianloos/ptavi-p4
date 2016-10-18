#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socketserver
import sys


class SIPRegisterHandler(socketserver.DatagramRequestHandler):

    client_dicc = {}
    
    def handle(self):        
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n") 

        line = self.rfile.read()
        data = line.decode('utf-8')
        chops = data.split(' ')
        if chops[0] == 'REGISTER':
            self.client_dicc[chops[1][4:]] = self.client_address[0]
            if chops[3][2:-1] == 'Expires':
                if chops[4][:-4] == '0':
                    del self.client_dicc[chops[1][4:]]
        print("El cliente nos manda:" + '\r\n' + data)
        print('IP: ', self.client_address[0])
        print('Puerto: ', self.client_address[1])
        print('Los datos del cliente son:', self.client_dicc)
        print()

if __name__ == "__main__":

    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Finalizado servidor")   
