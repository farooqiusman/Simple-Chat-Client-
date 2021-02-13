from socket import *
Host = str(INADDR_ANY)
port = 6969

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # will be able to reuse the address of the socket 

server.bind((Host, port))

server.listen(5)
print ('[+]binded\n[+]listening....')

while True:
	conn, addr = server.accept()
	print('[+]connected from: ', str(addr))
	conn.send(bytes("Welcome to the server!!", "utf-8")) # send a message to the client 
	conn.close()

print ('client disconnected')
server.shutdown()
server.close()
