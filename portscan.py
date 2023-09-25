#!/bin/pyton
import socket,sys

ip = input("Informe o ip do alvo: ")

def port_scan(alvo):

	for ip in range(1,256):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if (sock.connect_ex((alvo,ip)) ==0):
			print ("[+] Porta TCP Aberta:",ip)
		sock.close()
port_scan(ip)
