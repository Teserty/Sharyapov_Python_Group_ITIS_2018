import socket, threading
HOST = 'localhost'
PORT = 5023

CONNECTION_LIST = []
def accept_client():
	while True:
		cli_sock, cli_add = s.accept()
		uname = cli_sock.recv(1024).decode('utf8')
		print("Accepted: " + uname)
		CONNECTION_LIST.append((uname, cli_sock))
		thread_client = threading.Thread(target = broadcast_usr, args=[uname, cli_sock])
		thread_client.start()
def broadcast_usr(uname, cli_sock):
	while True:
		try:
			data = cli_sock.recv(1024).decode('utf8')
			if data:
				for i in CONNECTION_LIST:
					if i != (uname, cli_sock):
						i[1].send(("{0}:{1}".format(uname, data)).encode('utf8'))
		except Exception as x:
			print(x)
if __name__ == "__main__":
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(20)
	thread_ac = threading.Thread(target = accept_client)
	thread_ac.start()
	print("Ready")