#!/usr/bin/python

__author__ = 'Raphaël Doursenaud'

import socket

if __name__ == '__main__':

    udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    udpsock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    udpsock.sendto(bytes("TralalaUDP", 'utf-8'), ('<broadcast>', 3804))
    try:
        tcpsock.connect(('192.168.1.2', 3804))
        tcpsock.sendall(bytes("TralalaTCP", 'utf-8'))
    finally:
        tcpsock.close()
