import socket
import sys

TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024
file_name = sys.argv[1]


try:
    # initializa the socket and connect to the file port of the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, FILE_PORT))

    # send the file name
    sock.send(file_name)
    sock.close()

    print("Sending %s ..." % file_name)

    # open the file to read as a binary
    f = open(file_name, "rb")

    # initialize the socket connection to the data port of the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, DATA_PORT))

    # read and send the data
    data = f.read()
    sock.send(data)

finally:
    # close sock and file
    sock.close()
    f.close()
