import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%97%90%EC%8A%A4%ED%8C%8C+%EC%9C%88%ED%84%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img",attrs = {"class" : "_image _listImage"})
print(images)

for image in images:
    image_url = image["src"]
    print(image_url)