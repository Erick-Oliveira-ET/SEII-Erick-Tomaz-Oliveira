#!/usr/bin/python3

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 15000)
sock.bind(server_address)

sock.listen(1)

while True:
    print("Esperando por nova conexão!!")
    connection, client_address = sock.accept()

    try:
        while True:
            data = connection.recv(100)
            print(f"recebido: {data}")

            if data:
                print("reenviando mensagem para o cliente: ", client_address)
            else:
                print("não foi recebida nenhum dado de: ", client_address)
                break
    finally:
        connection.close()
