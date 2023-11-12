# 수의 자료형
print(5)
print(-10)
print(3.14)
print(100000000)
print(5+3)
print("5+3")

# 문자 자료형
print('풍선')
print("나비")
print("ㅋ"*9) # 문자 * 숫자도 가능!

# Boolean (BOOL형)
print(5>10)
print(5<10)
print(True)
print(not True) # not : 부정
print(not (5>10)) # True

# 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3 #Boolean

print("우리집 "+animal+"의 이름은 "+name+"에요")
print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요") # 문자열 자료가 아니라면 str()로 형변환
print(name,"는 ",age,"살이며, ",hobby,"을 아주 좋아해요") # +가 아닌 ,를 이용하면 형변환을 하지 않아도 되지만 띄어쓰기가 자동으로 들어감
print(name+ "는 어른일까요? "+str(is_adult))

# 주석
'''주석
ㄴ\ㄴㅇㅇㄹㄴㅇㄹ
ㄴㅇㄹㄹ'''

# 연산자
print(1+1)
print(3-2)
print(9*7)
print(6/3)
print(5%3)
print(10//3) # 몫 구하기
print(2**3) # 2의 3제곱

print(10>3) # True
print(4>=7) # False

print(3==3) #True
print(3!=3) #False
print(not(3==3)) #False

print((3>0) and (3<5)) #True
print((3>0) & (3<5)) #True

print((3>10) or (3>0)) #True
print((3>10) | (3>0)) #True

print(5>4>3) # True
print(5>4>7) # False

# 수식
number = 2 + 3 * 4
number += 2 # - * / % 다 가능

