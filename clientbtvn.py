import socket

def start_client():
    host = '127.0.0.1'
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        # Nhập hai số từ người dùng
        num1 = input("nhap so thu nhat: ")
        num2 = input("nhap so thu hai: ")
        # Gửi hai số đến server (dạng chuỗi 'num1,num2')
        message = f"{num1},{num2}"
        client_socket.sendall(message.encode())
        # Nhận kết quả từ server
        response = client_socket.recv(1024).decode()
        print(f"tong cua {num1} va {num2} la:{response}")
    
if __name__ == "__main__":
    start_client()
