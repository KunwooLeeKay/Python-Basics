import requests # 웹사이트에서 정보를 받아오기 위한 라이브러리
res = requests.get("http://google.com")
# print("응답코드 :",res.status_code) # 200이면 정상 작동

# if res.status_code == requests.codes.ok: # 또는 ==200이라고 해도 댐
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ",res.status_code,"]")

# res.raise_for_status() #문제가 있으면 이 문장에서 걍 종료하고 없다면 아래를 실행함.위의 코드를 아래처럼 2줄로 요약가능
# print("웹 스크래핑을 진행합니다.")

res.raise_for_status() # 이렇게만 적으면 끝 - 여기까지가 웹사이트정보를 가져온 거다.

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding = "utf8") as f:
    f.write(res.text) # 웹사이트 정보를 파일에 저장함. 해당 파일을 브라우져로 열면 비슷한 페이지가 뜬다.