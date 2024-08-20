import os
import requests
from bs4 import BeautifulSoup

query = "대구"
search_url = f"https://search.imbc.com/news?qt={query}"

download_folder = f"./{query}" # ./전기차

response = requests.get(search_url)
soup = BeautifulSoup(response.text, "html.parser")

image_tags = soup.find("ul", class_="list-type news-list")
lis = image_tags.find_all("li")



downloaded = 0

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

for img_tag in lis: 
    # 제목가져오기 
    # title = img_tag.find("span", class_="nw_tit ellipsis-multi").text
    # print(title)
    img_url = img_tag.find("img").get("src")
    print(img_url)
    img_data = requests.get(f"https:{img_url}").content
    img_name = os.path.join(download_folder, f"image_{downloaded + 1}.jpg")
    
    downloaded = downloaded + 1
    # downloaded += 1

    with open(img_name, "wb") as img_file:
        img_file.write(img_data)


print(f"{downloaded}개의 이미지를 다운로드 했습니다.")