import requests
from bs4 import BeautifulSoup

# Gửi yêu cầu tới trang web
url = 'https://imgflip.com/memetemplates?page=1'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tìm tất cả các thẻ div chứa hình ảnh meme template
    memes = soup.find_all('div', class_='mt-box')  # Cập nhật với class thực tế
    
    with open('meme_image_urls.txt', 'w', encoding='utf-8') as file:
        for meme in memes:
            # Lấy thẻ <img> trong mỗi div
            img_tag = meme.find('img')
            if img_tag:
                img_url = img_tag['src']
                if not img_url.startswith('https:'):
                    img_url = 'https:' + img_url  # Thêm phần https nếu thiếu
                file.write(f"{img_url}\n")
    
    print("Danh sách URL hình ảnh đã được ghi vào meme_image_urls.txt thành công.")
else:
    print(f"Không thể truy cập trang web. Mã lỗi: {response.status_code}")

