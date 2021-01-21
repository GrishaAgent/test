# lol
# kek

import socket
import json

print("SERVER\n")

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode("utf-8")
            my_dict = json.loads(data)
            print(my_dict)
            conn.sendall(bytearray(data, "utf-8"))
