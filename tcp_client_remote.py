from socket import *
from time import sleep

outer_host = '192.168.0.107'
outer_port = 33444
tcp_addr = (outer_host, outer_port)


def connector():
    while True:
        sleep(0.08)
        global used, data
        used = b'break'
        try:
            tcp_socket = socket(AF_INET, SOCK_STREAM)
            tcp_socket.connect(tcp_addr)
            tcp_socket.send(b'query')
            data = tcp_socket.recv(1024)
        except:
            print('Error! Connection refused!')
            sleep(1)
            break
        if data != b'break' or data != used:
            with open("exchange", "w") as file:
                file.write(str(data))
            with open("exchange", "r") as file:
                print("received: ", file.read()[2:-1])
            used = data
            tcp_socket.close()
        else:
            tcp_socket.close()
