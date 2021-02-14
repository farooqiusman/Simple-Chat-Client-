from socket import *
from pickle import *
from getpass import *

def _cerdientials(client):
	while True:
		username = input("Username: ")
		password = getpass().encode("utf-8")
		cerdientials = [username, password]
		client.send(dumps(cerdientials))
		break


def main():
	_cerdientials(client)
	from_server = ''
	while True:
		data = client.recv(1024)
		from_server += data.decode("utf-8")
		if not data:
			break
		
		print(from_server)		

if __name__=='__main__':
	client = socket(AF_INET, SOCK_STREAM)
	client.connect((gethostname(), 6969))
	main()

