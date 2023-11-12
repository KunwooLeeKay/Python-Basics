# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
""" # 이런식으로 여러 줄의 문장을 입력할 수도 있다.
print(sentence3)

# 슬라이싱
jumin = "990224-1234567" #파이썬에선 문자열을 입력하면 바로 배열처리가 된다.
print("성별 : " + jumin[7]) # 7번째 자료 (1)
print("연 : " + jumin[0:2]) # 0번째부터 2번째 전까지의 자료 (99) 
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 0은 생략해도 된다.
print("뒷자리 : " + jumin[7:]) # 비워두면 처음 or 끝
print("뒷자리 : " + jumin[-7:]) # -를 붙이면 뒤에서부터 센다. (맨 끝은 -1부터 시작이다. 0 아님)

# 문자열 처리 함수
python = "Python is Amazing"
print(python. lower()) # 다 소문자로
print(python. upper()) # 다 대문자로
print(python[0]. isupper()) # isupper : 대문자인지 판별
print(len(python)) # strlen
print(python. replace("Python", "C++")) # replace

place = python.index("n") #index : 문자열에서 해당 문자가 몇번째에 있는지(0부터 센다. 실제론 6번째인것!)
print(place)
place = python. index("n", place+1) # 시작위치를 앞선 n의 위치 다음부터로 설정한 후 찾기
print(place)

print(python. find("n")) # find : index와 같은 역할. index에서는 찾는게 없다면 에러, find에서는 없다면 -1 반환
print(python. find("C++")) # -1 반환

print(python. count("n")) # count : 문자열에서 해당 문자가 몇번 나왔는지 세줌

# 문자열 포맷
#  방법 1 : %d, %s 등등
print("나는 %d살입니다." %20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))
#  방법 2 : {}, .format() 이용
print("나는 {}살입니다.". format(20))
print("나는 {}색과 {}색을 좋아해요.". format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.". format("파란", "빨간")) # 중괄호에 숫자를 넣어서 format내의 배열 속에서 값을 지정할 수 있다.
#  방법 3 
print("나는 {age}살이며, {color}색을 좋아해요.". format(age = 20, color = "빨간")) # 변수처럼 선언도 가능
#  방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # 앞에 f를 쓰고 시작하면 실제 변수에서 가져다가 쓸 수 있다.
# print("나는 {age}살이며, {color}색을 좋아해요.". format(age, color)) 위의 방법 3처럼 하면 변수를 가져다가 쓸 수 없다.

# 탈출문자
print("백문이 불여일견 \n백견이 불여일타")
print("저는 '이건우'입니다.")
print("저는 \"이건우\"입니다.")
# 문장내에서 \\ = \
print("PS C:\\Users\\twoku\\OneDrive\\바탕 화면\\Python Workspace>")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # -> PineApple
# \b : backspace \t : tab
print(r"백문이 불여일견\n백견이 불여일타") # 이렇게 앞에 r을 붙이면 탈출문자건 뭐건 무시하고 작성 가능. 그냥 \n이 그대로 나옴
# 이는 주소같은거 적을 떄 위에서 처럼 \\을 안하고 그냥 앞에 r만 붙여서 써먹을 수 있음.