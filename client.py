import socket

def start_client():
    host = '127.0.0.1'
    port = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))  
        message = "my name is dat"  
        client_socket.sendall(message.encode())
        
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")  

if __name__ == "__main__":  
    start_client()