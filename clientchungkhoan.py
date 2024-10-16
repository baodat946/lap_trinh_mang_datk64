import socket

def get_stock_price(stock_code):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    client_socket.send(stock_code.encode())
    price = client_socket.recv(1024).decode()
    client_socket.close()

    return price

if __name__ == "__main__":
    stock_code = input("Nhập mã chứng khoán: ")
    price = get_stock_price(stock_code)
    print(f"Giá hiện tại của {stock_code}: {price}")
