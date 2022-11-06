import socket
import threading

HEADER = 64  # the first message will always be a 64 bytes message
PORT = 5050
SERVER = socket.gethostbyname(
    socket.gethostname()
)  # get the ip of the computer running the code
ADDR = (SERVER, PORT)
FORMAT = "utf-8"  # wanted result format
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)  # address family and type of transport
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)  # message comes in binary
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received!".encode(FORMAT))
    conn.close()


# handle the initialization of the server
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count()-1}")


print("[STARTING] server is starting...")
start()
