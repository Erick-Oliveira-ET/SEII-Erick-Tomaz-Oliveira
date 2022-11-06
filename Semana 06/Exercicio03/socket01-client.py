import socket
import time
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
file_name = sys.argv[1]

# initialize socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(file_name, (UDP_IP, UDP_PORT))
print("Sending %s ..." % file_name)

# open file as readable binary
f = open(file_name, "rb")
data = f.read(buf)
while data:
    if sock.sendto(data, (UDP_IP, UDP_PORT)):
        # send file data
        data = f.read(buf)
        time.sleep(0.02)  # Give receiver a bit time to save

# close socket and file operator
sock.close()
f.close()
