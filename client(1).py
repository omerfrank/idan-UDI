import socket                           # we will be using the class socket for connection
import pygame
client = socket.socket()                # make a socket for connection, using a constructor
client.connect(('127.0.0.1', 1729)) # connect the client to the server
                                        # the tuple is in the form (a,b):
                                        # a is a string of the server's ip
                                        # b is the int of the socket of the server
def checksum(str):
    num = 0
    for word in str:
        num += ord(word)
    return int(num)

client.recv(1024).decode()
times = 5
client.send("1".encode())

client.send(f"{1}# hello".encode())
i = f"{1}# hello"
client.send(f"{checksum(i)}".encode())





















client.close()                          # close the socket so that it is free for other programs
