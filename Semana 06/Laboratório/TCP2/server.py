#!/usr/bin/python3

import socket
import sys
import argparse

host = "localhost"
data_payload = 2048
backlog = 5


def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = (host, port)
    print(f"Starting up echo server on {server_address}")

    sock.bind(server_address)

    sock.listen(backlog)

    while True:
        print("Waiting to receive message from client")
        client, address = sock.accept()
        data = client.recv(100)

        if data:
            print(f"Data: {data}")

            client.send(data)
            print(f"sent {data} bytes back to {address}")
        client.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket Server Example")
    parser.add_argument("--port", action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port

    echo_server(port)
