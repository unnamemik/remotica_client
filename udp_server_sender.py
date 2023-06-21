from socket import *
from time import sleep

inner_host = '192.168.0.112'
inner_port = 8266
udp_addr = (inner_host, inner_port)
udp_socket = socket(AF_INET, SOCK_DGRAM)


def udp_sender():
    while True:
        sleep(0.08)
        with open("exchange", "r") as file:
            replay_data = file.read()[2:-1]
            print("send: ", replay_data)
            udp_socket.sendto(replay_data.encode(), udp_addr)
