import socket
import time,sys
from multiprocessing import Process

HOST = ''
PORT = 8001
BUFFER_SIZE = 1024
def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        while True:
            conn,addr = s.accept()
            p = Process(target=handle_echo,args=(addr,conn))
            p.daemon = True
            p.start()
            print("Started Process", p)
            
def handle_echo(addr, conn):
    print('Connected by', addr)
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    conn.sendall(full_data)
    conn.close()
if __name__ == "__main__":
    main()