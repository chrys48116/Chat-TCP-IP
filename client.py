import socket
import threading

ServerIP = ''
PORT = int()
username = ''

def conectar():
    global client
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        client.connect((ServerIP,PORT))
        print(f'Connected Successfully to {ServerIP}:{PORT}')
        
    except:
       print(f'ERROR: Please review your input: {ServerIP}:{PORT}')
               
messageRecv = ''
def receiveMessage():
    global messageRecv
    while True:
        try:
            message = client.recv(2048).decode('ascii')
            if message=='getUser':
                client.send(username.encode('ascii'))
            else:
                print('-> '+message)
                messageRecv = message
        except:
            print('ERROR: Check your connection or server might be offline')


messegeSend = ''
def sendMessage():
    message = messegeSend 
    while True:
        client.send(message.encode('ascii'))
        break

thread1 = threading.Thread(target=receiveMessage,args=()) 
thread2 = threading.Thread(target=sendMessage,args=())

#thread1.start()
#thread2.start()


  