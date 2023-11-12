import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs = {"class" : "title"}) # soup객체 중 클래스명이 title인 a element를 다 가져옴(find_all)

for cartoon in cartoons:
    print(cartoon.get_text())

