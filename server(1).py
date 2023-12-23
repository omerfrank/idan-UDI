import socket                           # we will be using the class socket for connection

def checksum(str):
    num = 0
    for word in str:
        num += ord(word)
    return num
server = socket.socket()                # create a socket object to use for connection
server.bind(('127.0.0.1', 1729))    # tell the server to prepare to listen on the ip A, on the socket B
                                        # the tuple is in the form (A,B):
                                        # A is a string of the server's ip
                                        # B is the int of the socket to listen too
server.listen()                         # tell the server to start listening for clients and wait till a client connects
client, address = server.accept()       # reaching this line means that a client wants to connect,
                                        # server.accept() returns a tuple (A,B)
                                        # A is the client's socket object
                                        # B is the client's addres (in the same form as in line 4)

client.send("how many mes?".encode())
times = int(client.recv(1024).decode())
messeges = []

#get all meseges
for i in range(1, times):
    messeges.append(client.recv(1024).decode())
counter = 1

#order check and double
for i in range(1,len(messeges),2):

    if (messeges[i][0,i.find("#")] != f"{counter}"):
        print("wrong order")
    counter+=1
# check size
for i in range(1,len(messeges)/2,2):
    if checksum(messeges[i]) != int(messeges[i+1]):
        print("lost info")













client.close()                          # close the sockets so that it is free for other programs
server.close()


