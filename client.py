from socket import *
	
client = socket(AF_INET, SOCK_STREAM)
client.connect((gethostname(), 6969))

from_server = ''
while True:
	data = client.recv(1)
	if not data:
		break
	from_server += data.decode("utf-8")

print(from_server)

