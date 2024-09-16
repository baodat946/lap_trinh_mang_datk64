import requests
from bs4 import BeautifulSoup

# Gửi yêu cầu tới trang web
url = 'https://imgflip.com/i/92g7tr'  # Thay đổi URL này
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Lấy tiêu đề trang
    title = soup.title.string if soup.title else 'Không tìm thấy tiêu đề.'
    
    # Ghi tiêu đề vào tệp text.txt
    with open('text.txt', 'w', encoding='utf-8') as file:
        file.write(f"Tiêu đề: {title}\n\n")
    
    print("Dữ liệu tiêu đề đã được ghi vào text.txt thành công.")
    
# URL hình ảnh bạn muốn tải
image_url = 'https://i.imgflip.com/92g8h3.jpg'  # Cập nhật URL hình ảnh

# Gửi yêu cầu tải ảnh về
image_response = requests.get(image_url)

if image_response.status_code == 200:
    # Lưu ảnh vào file
    with open('yo_dawg_meme.jpg', 'wb') as image_file:
        image_file.write(image_response.content)
    print("Hình ảnh đã được tải về thành công!")
else:
    print(f"Không thể tải hình ảnh. Mã lỗi: {image_response.status_code}")


