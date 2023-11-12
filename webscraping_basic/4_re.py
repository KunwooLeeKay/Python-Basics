# re 는 정규식이라는 뜻. ex) 이메일 : twokunwoo224@naver.com, 주민번호 : 990224 - 1111111 등
# IP주소 : 192.168.0.1

import re
# 예를 들어 ca?e만 알고 있는데 이게 무슨 단어인지 모른다고 하자. care, cafe, case등등 가능

# .(ca.e) : 하나의 문자를 의미 -> care, cafe, case (o) | caffe (x)
# ^ (^de): 문자열의 시작 -> desk, destination (o) | fade (x)
# $ (se$) : 문자열의 끝 -> case, base(o) | face(x)

# m = p.match("case")
# print(m.group()) # 매치되지 않으면 에러가 발생
# m = p.match("caffe")
# print(m.group())

p = re.compile("세대수")
wee = ['세대수 744세대(총10개동) 저/최고층 12층/12층', '사용승인일 1984년 10월 23일 총주차대수 744대(세대당 1대)', '용적률 165% 건폐율 -', '건설사 한양', '난방 지역난방, 열병합', '관리사무소 02-423-7427', '주소', '서울시 송파구 송파동 151', '서울시 송파구 가락로 192', '면적', '87㎡, 105㎡, 131㎡, 150㎡, 172㎡']
print(p.search(wee[0]).group())

p = re.compile("ca.e")
def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:",m.string) # 입력받은 문자열 반환
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작/끝 index
        
    else:
        print("매칭되지 않음")

m = p.match("careless") # 얘는 매칭이 된다. 주어진 문자열의 처음부터 일치하는지확인하기 때문에 care까지만 보고 매칭된다고 하고 care반환
print_match(m)

m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인 # 얘를 m.group돌리면 care로 출력. match로 하면 매칭 안됨
print_match(m)

lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)


# 정리
# 1. p = re.compile("원하는 형태") - 원하는 형태 : 정규식! 더 필요하면 w3schools에 python에 regular expression 찾기
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환