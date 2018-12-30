import socket, threading
HOST = 'localhost'
PORT = 5023
def receive():
    while True:
        print(s.recv(1024).decode('utf8')+'\n')
if __name__ == "__main__":   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))    
    print('Connected to remote host...')
    uname = input('Enter your name to enter the chat > ')
    s.send(uname.encode('utf8'))
    thread_receive = threading.Thread(target = receive)
    thread_receive.start()
    while True:
        msg = input()
        s.send(msg.encode('utf8'))