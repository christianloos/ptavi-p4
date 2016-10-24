#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socketserver
import sys
import json
import time


class SIPRegisterHandler(socketserver.DatagramRequestHandler):

    client_list = []

    def handle(self):
        self.json2registered()

        line = self.rfile.read()
        data = line.decode('utf-8')
        chops = data.split(' ')
        hora = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))

        if chops[0] == 'REGISTER':
            exp_time = int(chops[3][:-4])
            client = [chops[1][4:],
                      {"address": self.client_address[0],
                       "expires": str(hora) + ' +' + str(exp_time)}]
            if exp_time == 0:
                for cli in self.client_list:
                    if cli[0] == chops[1][4:]:
                        self.client_list.remove(cli)
            if exp_time > 0:
                for cli in self.client_list:
                    if cli[0] == chops[1][4:]:
                        self.client_list.remove(cli)
                self.client_list.append(client)

        print("El cliente nos manda:" + '\r\n' + data)
        print('IP: ', self.client_address[0])
        print('Puerto: ', self.client_address[1])
        print()
        print('Los clientes existentes son:', self.client_list)
        print('-----------------------')

        self.register2json()
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

    def register2json(self):
        json_file = open('registered.json', 'w')
        json.dump(self.client_list, json_file, indent='\t')

    def json2registered(self):
        try:
            with open('registered.json') as client_file:
                self.client_list = json.load(client_file)
        except:
            self.register2json()

if __name__ == "__main__":

    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Finalizado servidor")
