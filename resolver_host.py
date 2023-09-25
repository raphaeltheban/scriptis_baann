#!/bin/python3
import socket,sys

host = input("Digite o site: ")

print (host, "--->", socket.gethostbyname(host))
