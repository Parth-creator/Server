import socket
import threading

SERVER = '192.168.1.10'
PORT = 9998
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
     
    bool = conn.recv(1024).decode(FORMAT)
    
    if bool == 'True':
        name = conn.recv(1024).decode(FORMAT)
    
    elif bool == 'False':
        sign_in_up = conn.recv(1024).decode(FORMAT)
        
        if sign_in_up == 'I':

            email_file = open('email.txt', 'r')
            password_file = open('password.txt', 'r')
            username_file = open('username.txt', 'r')
                        
            email_list = email_file.readlines()
            password_list = password_file.readlines()
            username_list = username_file.readlines()
        
            while True:
        
                email_input = conn.recv(1024).decode(FORMAT)
                password_input = conn.recv(1024).decode(FORMAT)
                
                email_input = email_input + '\n'
                password_input = password_input + '\n'
                
                if email_input in email_list:
                    if password_list[email_list.index(email_input)] == password_input:
                        
                        conn.send('True'.encode(FORMAT))
                        username = username_list[email_list.index(email_input)].rstrip('\n')
                        name = username
                        conn.send(username.encode(FORMAT))
                        
                        break
                        
                    else:
                        conn.send('False'.encode(FORMAT))
                        pass
                        
                else:
                    conn.send('False'.encode(FORMAT))
                    pass
                
            #print(email_input)
            #print(password_input)
            #print(email_list)
            #print(password_list)
            #print(username_list)
 
            
        elif sign_in_up == 'U':
            email_input = conn.recv(1024).decode(FORMAT)
            password_input = conn.recv(1024).decode(FORMAT)
            username_input = conn.recv(1024).decode(FORMAT)
            
            email_file = open('email.txt', 'a')
            password_file = open('password.txt', 'a')
            username_file = open('username.txt', 'a')
            
            email_file.write(email_input + '\n')
            password_file.write(password_input + '\n')
            username_file.write(username_input + '\n')
            
            email_file.close()
            password_file.close()
            username_file.close()
            
            name = conn.recv(1024).decode(FORMAT)

    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True

    while connected:
        msg = conn.recv(1024).decode()

        if msg == DISCONNECT_MSG:
            connected = False

        for i in clients:
            if i != conn:
                i.send(f"{name}: ".encode(FORMAT) + msg.encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        clients.insert(0, conn)
        clients[0].send("Welcome to the server".encode(FORMAT))
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


print("[STARTING ] server is starting...")
start()
