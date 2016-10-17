#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socketserver
import sys


class SIPRegisterHandler(socketserver.DatagramRequestHandler):

    def handle(self):        
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n") 

        client_data = {}
        line = self.rfile.read()
        data = line.decode('utf-8')
        chops = data.split(' ')
        if chops[0] == 'REGISTER':
            client_data[chops[1]] = chops[2]
            client_data['ip'] = self.client_address[0]
            
            if chops[4] == 'Expires':
                del client_data['sip', 'ip']
        
        print("El cliente nos manda:" + '\r\n' + data)
        print('IP: ', self.client_address[0])
        print('Puerto: ', self.client_address[1])
        print('Los datos del cliente son:', client_data)
        print()

if __name__ == "__main__":

    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Finalizado servidor")   
