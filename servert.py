import socket
import threading

# Hàm tính tỷ lệ vàng
def golden_ratio(number):
    return number * 1.618

# Hàm xử lý phép tính
def calculate_expression(expression):
    try:
        # Đánh giá biểu thức (cộng, trừ, nhân, chia)
        result = eval(expression)
        return result
    except:
        return "Lỗi: Biểu thức không hợp lệ."

# Hàm xử lý kết nối client
def handle_client(client_socket):
    try:
        # Nhận dữ liệu từ client
        data = client_socket.recv(1024).decode('utf-8')

        # Kiểm tra nếu là số thì tính tỷ lệ vàng, nếu là biểu thức thì thực hiện tính toán
        if data.isdigit():
            number = float(data)
            result = golden_ratio(number)
        else:
            result = calculate_expression(data)

        # Gửi kết quả lại cho client
        client_socket.send(str(result).encode('utf-8'))
    except ValueError:
        client_socket.send("Lỗi: Dữ liệu không hợp lệ.".encode('utf-8'))
    finally:
        client_socket.close()

# Thiết lập server
def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server đang lắng nghe...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Kết nối từ {address}")

        # Tạo một luồng mới để xử lý client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    server_program()