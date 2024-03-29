#!/usr/bin/python3
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

for item in range(10):
    print("\n->", item + 1)
    data, addr = sock.recvfrom(1024)
    print("received message: %s" % data)
