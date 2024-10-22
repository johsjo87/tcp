import socket

HOST = '127.0.0.1'
PORT = 12345

# Skapa en TCP-socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.bind((HOST, PORT))
    server_sock.listen(2)  # Väntar på 2 klienter
    print(f"Väntar på anslutning från {HOST}:{PORT}")
    print("Väntar på 2 spelare") 
    
    client1_sock, addr1 = server_sock.accept()
    print(f"Spelare 1 ansluter via {addr1}")
    
    client2_sock, addr2 = server_sock.accept()
    print(f"Spelare 2 ansluter via: {addr2}")
    
    player1_choice = client1_sock.recv(1024).decode('utf-8')
    print(f"Spelare 1 valde: {player1_choice}")
    
    player2_choice = client2_sock.recv(1024).decode('utf-8') 
    print(f"Spelare 2 valde: {player2_choice}")
    
    def winner(choice1, choice2):
        if choice1 == choice2:
            return "Oavgjort"
        elif (choice1 == "sten" and choice2 == "sax") or\
            (choice1 == "sax" and choice2 == "påse") or \
            (choice1 == "påse" and choice2 == "sten"):
            return "Spelare 1 vinner"
        else:
            return "Spelare 2 vinner"
        
    result = winner(player1_choice, player2_choice)
    print(f"Resultat: {result}")    
    
    client1_sock.sendall(result.encode('utf-8'))
    client2_sock.sendall(result.encode('utf-8'))

# Stäng anslutningar
client1_sock.close()
client2_sock.close()

