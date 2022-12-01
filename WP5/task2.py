import socket
import threading
from time import sleep

sock = socket.socket()
# addr = ("51.250.16.220", 55555)
addr = ("127.0.0.1", 65432)
sock.connect(addr)

data_out = input("Enter ypur name: ")
sock.send(data_out.encode('ascii'))

def recieving():
    while True:
        data_chunk = sock.recv(1024)
        if data_chunk:
            print(data_chunk)

def send():
    data_out = input("\n")
    sock.send(data_out.encode('ascii'))
    return data_out

rec_thread = threading.Thread(target=recieving)
rec_thread.start()


while True:
    # end_word = ""
    if send() == "exit":
        break

sock.close()
    

# s = threading.Thread(target=send)
# s.start()
# sock.close()