import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
    client_sock.connect((HOST, PORT))
    
    choice = input("Gör ditt val här välj: sten sax eller påse: ").strip().lower()
    
    client_sock.sendall(choice.encode('utf-8'))
    
    result = client_sock.recv(1024).decode('utf-8')
    print(f"resultat: {result}")
    
    
    
    