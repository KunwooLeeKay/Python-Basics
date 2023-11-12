# if문
#weather = input("오늘 날씨는 어때요? ")
weather = "맑음"
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")

#temp = int(input("기온은 어때요? ")) # input은 항상 문자열로 값을 입력받는다. 밖에 int()로 감싸주면 temp에 int형 데이터를 넣을 수 있다.
temp = -3000
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요")

# for문
for waiting_no in [0,1,2,3,4,]:
    print("대기번호 : {0}". format(waiting_no))

for waiting in range(5): # range : 0이상 5미만.
#waiting에 0을 넣고 실행 후 1넣고 실행 후 2넣고 .... 해서 5번 반복하는 반복문
    print("hi")

starbucks = ["iron man", "Thor", "Groot"] # 기존 배열을 사용한 for문
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다.". format(customer))



# While문
# 만약 5번 호출했는데 안오면 커피를 버리는 카페
index = 5
while index >= 1:
    print("고객님 커피가 준비되었습니다. {}번 남았어요.". format(index))
    index -= 1
    if index == 0:
        print("커피는 버릴게요.")

# 무한 반복문
index = 1
while True:
    print("고객님 커피 나왔어요!. 호출 {}회 차". format(index))
    index += 1
    if index == 10 : break

customer = "Thor"
person = "Unknown"

while person != customer :
    print("{}, 커피가 준비되었습니다.". format(customer))
    # person = input("이름이 어떻게되세요? ")
    person = "Thor"

# continue와 break
absent = [2,5] # 결석
no_book = [7] # 책을 안가져옴
for student in range(1, 11):
    if student in absent : 
        continue # 만약 해당 학생이 결석이라면, 다음 반복 실행(아래의 print를 건너뜀)
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와". format(student)) 
        break # 해당 학생이 책을 안가져오면 수업 끝
    print("{0}아, 책을 읽어봐.". format(student))

# 한줄 for문
 # 출석번호가 1,2,3,4...이렇게 가는데 101, 102, 식으로 100을 붙이기로 할때
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

 # 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am Groot"]
students = [len(i) for i in students]
print(students)

 # 학생 이름을 대문자로 변환
students = ["Lee", "Kim", "Jung"]
students = [i.upper() for i in students]
print(students)