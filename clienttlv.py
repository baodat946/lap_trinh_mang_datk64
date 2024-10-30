import socket

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Nhập số hoặc biểu thức từ bàn phím
    expression = input("Nhập vào một số hoặc một biểu thức phép toán (vd: 2 + 3, 5 * 4): ")

    # Gửi biểu thức cho server
    client_socket.send(expression.encode('utf-8'))

    # Nhận kết quả từ server
    result = client_socket.recv(1024).decode('utf-8')
    print(f"Kết quả: {result}")

    client_socket.close()

if __name__ == "__main__":
    client_program()
