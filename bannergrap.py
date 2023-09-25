#!/bin/python3

import socket

ip = input("Digite o IP: ")
porta = int(input("Porta: "))

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect((ip,porta))
banner = meusocket.recv(1024)
print (banner)

userencode = str.encode("USER raphael\n")
meusocket.send(userencode)
banner = meusocket.recv(1024)
print (banner)

passencode = str.encode("PASS raphael\n")
meusocket.send(passencode)
banner = meusocket.recv(1024)
print (banner)
