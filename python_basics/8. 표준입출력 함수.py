# 표준 입출력
print ("Python" , "Java" , "Javascript") # 이건 띄어쓰기
print ("Python" + "Java" + "Javascript") # 이건 붙여쓰기
print ("Python" , "Java" , "Javascript", sep = " vs ") # sep(separate) = ""를 통해 콤마부분에 넣을 것을 설정할 수 있음
print ("Python" , "Java" , "Javascript", sep = " vs ", end = "?") # end = ""를 통해 문장의 끝에 있던 \n을 바꿔줄 수 있음
print()

import sys
print ("Python" , "Java" , "Javascript", file = sys. stdout)
print ("Python" , "Java" , "Javascript", file = sys. stderr) # 똑같이 출력되는것 처럼 보여도 이건 에러처리에 유용한 출력방식.

# 왼쪽, 오른쪽 정렬 : .ljust(칸수) / .rjust(칸수)
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep = " : ")

#  1, 2, 3 같은 수를 001, 002, 003과 같이 바꾸기 : zfill(칸수)
for num in range(1,11):
    print("대기번호 : " + str(num).zfill(3))

# 표준 입력함수 : input 항상 문자열 형태로 저장됨 
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")

# 다양한 출력 포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리의 공간을 확보
print("{0: >10}". format(500)) # 0: 다음에 띄워쓰기 한칸 = 빈공간, > = 오른쪽 정렬, 10 = 10자리
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}". format(500))
print("{0: >+10}". format(-500))
# 왼쪽정렬, 빈공간은 _로 채움
print("{0:_<10}". format(500))
# 3자리마다 ,를 찍어주기
print("{0:,}".format(1000000000))
# 위에다가 추가로 부호도 붙이고, 30자리 확보하고 빈공간엔 ^
print("{0:^<+30,}".format(1000000000))
# 소수점 출력
print("{0: 3.3f}". format(5/3))