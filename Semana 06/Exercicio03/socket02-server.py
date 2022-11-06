import socket

TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
timeout = 3
buf = 1024


# initializing the file port to the server
sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_f.bind((TCP_IP, FILE_PORT))
sock_f.listen(1)

# initializing the data port to the server
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind((TCP_IP, DATA_PORT))
sock_d.listen(1)


while True:
    # accept connection to the file port
    conn, addr = sock_f.accept()
    data = conn.recv(buf)  # get file name transmitted
    if data:
        print("File name:", data)
        file_name = data.strip()

    f = open(file_name, "wb")  # create a binary file with the name passed

    conn, addr = sock_d.accept()  # accept data connection
    while True:
        data = conn.recv(buf)  # get file data transmitted
        if not data:
            break
        f.write(data)  # writes the data transmitted in the file

    print("%s Finish!" % file_name)
    f.close()  # close file
