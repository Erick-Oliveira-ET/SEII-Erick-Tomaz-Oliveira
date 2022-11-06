import socket
import select

UDP_IP = "127.0.0.1"
IN_PORT = 5005
timeout = 3

# initialize socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True:
    # get data from socket
    data, addr = sock.recvfrom(1024)

    # if there isn't any data start the loop again
    if not data:
        continue

    # get file name if any
    print("File name:", data)
    file_name = data.strip()

    # create and open a file with the name passed as as writable binary
    f = open(file_name, "wb")

    while True:
        # Wait until one or more file descriptors are ready for some kind of I/O.
        ready = select.select([sock], [], [], timeout)

        if ready[0]:
            # get and write data from socket to file
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
            print("%s Finish!" % file_name)
            f.close()
            break
