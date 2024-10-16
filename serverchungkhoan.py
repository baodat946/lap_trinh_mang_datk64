import socket
import requests
from bs4 import BeautifulSoup

def get_stock_price(stock_code):
    url = f"https://iboard.ssi.com.vn/stock/{stock_code}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tìm giá chứng khoán trong trang (cần điều chỉnh nếu cấu trúc HTML thay đổi)
    price_tag = soup.find('div', class_='current-price')  # Giả sử có class như vậy
    if price_tag:
        return price_tag.text.strip()
    return "Giá không tìm thấy."

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server đang chạy...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Kết nối từ {addr}")
        stock_code = client_socket.recv(1024).decode()
        print(f"Mã chứng khoán nhận được: {stock_code}")

        price = get_stock_price(stock_code)
        client_socket.send(price.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
