import requests
from bs4 import BeautifulSoup
import json

# Gửi yêu cầu GET đến trang VnExpress
response = requests.get('https://vnexpress.net')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all('h2', class_='title', limit=5)

    # Lưu tiêu đề vào danh sách
    title_list = [title.get_text(strip=True) for title in titles]

    # Ghi tiêu đề vào tệp JSON
    with open('titles.json', 'w', encoding='utf-8') as f:
        json.dump(title_list, f, ensure_ascii=False, indent=4)
    
    print("Tiêu đề đã được lưu vào titles.json")
else:
    print(f"Failed: {response.status_code}")
