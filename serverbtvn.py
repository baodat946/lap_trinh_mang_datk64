import socket

def start_server():
    host = '127.0.0.1'
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"SERVER is listening on {host}:{port}")
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024).decode()  # Nhận dữ liệu từ client
            if data:
                # Tách hai số từ dữ liệu nhận được
                num1, num2 = map(int, data.split(','))
                # Tính tổng
                result = num1 + num2
                # Gửi kết quả về client
                conn.sendall(str(result).encode())

if __name__ == "__main__":
    start_server()
