from socket import *
from pickle import *

def send_msg(socket, msg):
	for sock in connections:
		if sock != server and socket != sock:
			try:
				sock.send(msg)
			except:
				print("broken socket")
				sock.close()
				connections.remove(sock)

if __name__ == '__main__':

	Host = str(INADDR_ANY)
	port = 6969
	# making the server
	server = socket(AF_INET, SOCK_STREAM)
	server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # will be able to reuse the address of the socket 
	server.bind((Host, port))
	server.listen(5)
	connections = []
	buffer = 4096
	connections.append(server)
	print("Server started...")


	username = ''
	password = ''
	while True:
		for socket in connections:
			if socket == server:
				conn, addr = server.accept()
				print('[+] connected from: ', str(addr))
				connections.append(conn)
				_list = loads(conn.recv(buffer))
				username = _list[0]
				password = _list[1]
				print(username, password)
			else:
				# data is coming in from a client
				try:
					_list = loads(socket.recv(buffer))
					data = _list[0]
					send = _list[1]
					if data:
						send_msg(socket, data)

				except:
					print("Client %s is offline" % str(addr))
					socket.close()
					connections.remove(socket)
					continue
	server.close()
