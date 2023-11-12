# pip install beautifulsoup4, lxml 함

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 이렇게 하면 네이버 웹툰 페이지의 모든 html정보를 가져옴
# print(soup.title) # title의 모든 정보 가져옴
# print(soup.title.get_text()) # title의 텍스트만 가져옴
# print(soup.a) # soup 객체에서 첫번째 a에 해당하는 값을 가져옴
# print(soup.a.attrs) # attribute : a element의 속성 정보를 가져옴
# print(soup.a["href"]) # a element 의 href 속성 정보를 가져올 수 있다.
 # 이건 사실 해당 페이지에 대해서 잘 알고 있을때나 쓰는거. 모를땐 find씀

print(soup.find("a", attrs = {"class" : "Nbtn_upload"})) # class가 Nbtn_upload에 해당하는 첫번째 a element만 찾아줌
print(soup.find(attrs = {"class" : "Nbtn_upload"})) # class = Nbtn_upload 인 어떤 elemet를 찾아줌

print(soup.find("li", attrs = {"class":"rank01"}))
rank1 = soup.find("li", attrs = {"class":"rank01"})
print(rank1.a.get_text()) # 이렇게 쓰면 text만 가져옴
# print(rank1.next_sibling) 줄바꿈 정보땜에 한번만 하면 안될 수도 있음
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
print(rank1.parent) # 이렇게 태그간에 부모, 자식 관계로 왔다갔다 가능

rank2 = rank1.find_next_sibling("li") # 이렇게 넣으면 위처럼 줄바꿈 정보를 무시하고 다음 li태그에 해당하는 정보 가져옴
# 이렇게 하면 두번씩 쓰는 그런거 안해도 댐
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

print(rank1.find_next_siblings("li")) # siblings로 쓰면 모든 다음걸 가져옴

webtoon  = soup.find("a", text = "전지적 독자 시점-058. Ep.13 왕들의 전쟁 (2)") # 이렇게 텍스트값으로 정보 가져오기도 가능하다.
print(webtoon)