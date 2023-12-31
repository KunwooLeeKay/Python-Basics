import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=335885"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("td", attrs = {"class" : "title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

# 만화 제목과 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 가져오기
total_rates = 0
cartoons = soup.find_all("div", attrs = {"class" : "rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates+=float(rate)
print("전체 점수 : ",total_rates)
print("평균 점수 : ", total_rates / len(cartoons))

# 더 자세한 내용은 구글에 beautifulsoup검색해서 한국어 번역버전도 볼 수 있음