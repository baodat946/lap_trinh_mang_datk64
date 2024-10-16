import socket

def start_server():
    host = '127.0.0.1'
    port = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))  
        server_socket.listen()
        print(f"Server is listening on {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024).decode()
            if data:
                name = data.split("is")[-1].strip()
                response = f"Hello {name}"
                conn.sendall(response.encode())
                
if __name__ == "__main__":
    start_server()