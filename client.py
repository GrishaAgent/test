import socket
import json

print("CLIENT\n")

HOST = '127.0.0.1'
PORT = 65432

my_dict = {"x": 3, "y": 4}
my_json = json.dumps(my_dict)
print(my_json)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytearray(my_json, "utf-8"))
    data = s.recv(1024)

print('Received', repr(data))
