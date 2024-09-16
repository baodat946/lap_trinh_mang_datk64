import requests
from bs4 import BeautifulSoup

# List of URLs
urls = [
    'https://i.imgflip.com/4/30b1gx.jpg',
    'https://i.imgflip.com/4/1g8my4.jpg',
    'https://i.imgflip.com/4/1ur9b0.jpg',
    'https://i.imgflip.com/4/3oevdk.jpg',
    'https://i.imgflip.com/4/261o3j.jpg',
    'https://i.imgflip.com/4/3lmzyx.jpg',
    'https://i.imgflip.com/4/22bdq6.jpg',
    'https://i.imgflip.com/4/24y43o.jpg',
    'https://i.imgflip.com/4/1c1uej.jpg',
    'https://i.imgflip.com/4/28j0te.jpg',
    'https://i.imgflip.com/4/26jxvz.jpg',
    'https://i.imgflip.com/4/2fm6x.jpg',
    'https://i.imgflip.com/4/46e43q.jpg',
    'https://i.imgflip.com/4/9ehk.jpg',
    'https://i.imgflip.com/4/5c7lwq.jpg',
    'https://i.imgflip.com/4/23ls.jpg',
    'https://i.imgflip.com/4/43a45p.jpg',
    'https://i.imgflip.com/4/54hjww.jpg',
    'https://i.imgflip.com/4/2odckz.jpg',
    'https://i.imgflip.com/4/345v97.jpg',
    'https://i.imgflip.com/4/1tl71a.jpg',
    'https://i.imgflip.com/4/1otk96.jpg',
    'https://i.imgflip.com/4/1ihzfe.jpg',
    'https://i.imgflip.com/4/1jwhww.jpg',
    'https://i.imgflip.com/4/1bij.jpg',
    'https://i.imgflip.com/4/1b42wl.jpg',
    'https://i.imgflip.com/4/2ybua0.jpg',
    'https://i.imgflip.com/4/1bhk.jpg',
    'https://i.imgflip.com/4/2gnnjh.jpg',
    'https://i.imgflip.com/4/3pdf2w.jpg',
    'https://i.imgflip.com/4/21uy0f.jpg',
    'https://i.imgflip.com/4/26am.jpg',
    'https://i.imgflip.com/4/2za3u1.jpg',
    'https://i.imgflip.com/4/1wz1x.jpg',
    'https://i.imgflip.com/4/gk5el.jpg',
    'https://i.imgflip.com/4/46hhvr.jpg',
    'https://i.imgflip.com/4/1o00in.jpg',
    'https://i.imgflip.com/4/38el31.jpg',
    'https://i.imgflip.com/4/m78d.jpg',
    'https://i.imgflip.com/4/gtj5t.jpg'
]

for url in urls:
    # Extract the image ID from the URL
    image_id = url.split('/')[-1].split('.')[0]

    # Send a request to the image page
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get the title of the image
        title = soup.title.string if soup.title else 'Không tìm thấy tiêu đề.'

        # Write the title to a text file
        with open(f'{image_id}.txt', 'w', encoding='utf-8') as file:
            file.write(f"Tiêu đề: {title}\n\n")
        print(f"Tiêu đề của hình ảnh {image_id} đã được ghi vào {image_id}.txt thành công.")

        # Save the image to a file
        with open(f'{image_id}.jpg', 'wb') as image_file:
            image_file.write(response.content)
        print(f"Hình ảnh {image_id} đã được tải về thành công!")
    else:
        print(f"Không thể tải hình ảnh {image_id}. Mã lỗi: {response.status_code}")