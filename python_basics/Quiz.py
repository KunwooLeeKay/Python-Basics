# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램

url = "http://studypythonalot.com"
# pw1 = url[7:12]
# pw2 = len(pw1)
# pw3 = pw1.count('e')
# print("비밀번호 : " +pw1[0:3] + str(pw2) + str(pw3) + "!") 처음에 내가 한 방식

my_str = url.replace("http://","") #replace 이용
print(my_str) # 규칙 1
my_str = my_str[:my_str.index('.')] # 규칙 2 index이용 '.' 앞까지만 따옴
print(my_str)
password = my_str[0:3] + str(len(my_str)) + str(my_str. count('e')) + "!" # 변수에 '+'이용해 붙임
print("\"{}\" 사이트의 비밀번호는 \"{}\"입니다. ". format(url, password))


# Quiz) 당첨자 추첨 프로그램

# from random import *
# id_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(" === 당첨자 발표 ===")
# chicken = sample(id_list, 1)
# print("치킨 당첨자 : " + str(chicken))
# # id_list. remove(chicken) 이거 왜 안될까..?
# print("커피 당첨자 : " + str(sample(id_list, 3)))
# print(" === 축하합니다 ===")
from random import *
users = range(1, 21) # range : 1 이상 21 미만의 숫자 생성
# print(type(users))
users = list(users) # list형 자료로 변환
shuffle(users)
winners = sample(users, 4)
# print(type(winners))
print("=== 당첨자 발표 ===")
print("치킨 당첨자 : {0}". format(winners[0]))
print("커피 당첨자 : {0}". format(winners[1:4]))
print("=== 축하합니다 ===")

# Quiz) 택시기사 문제
from random import *
i = 1
count = 0
while i < 51:
    customer = {i : randrange(5, 51)}
    if(4 < customer.get(i) < 16):
        print("[o] {}번째 손님 (소요시간 : {})". format(i, customer.get(i)))
        count += 1
    else :
        print("[ ] {}번째 손님 (소요시간 : {})". format(i, customer.get(i)))
    i +=1
print("탑승 승객 수 : " + str(count))

# Quiz) 표준 체중 문제
height = 175
gender = "남자"

def std_weight(height, gender):
    if gender == "남자":
        return ((height/100)*(height/100)*22)
    elif gender == "여자":
        return (height*height*21/10000)
    else: print("잘못된 입력!")

std = round(std_weight(height, gender)*100)/100
# std = round(std_weight(height, gender), 2) 이렇게 적으면 소수점 둘째자리까지 나타내는 것으로 할 수 있다.
print("키 {}cm {}의 표준 체중은 {}kg 입니다.". format(height, gender, std))