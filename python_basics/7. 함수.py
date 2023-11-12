# 함수 -> def 함수이름(): 실행 내용

def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

def deposit(balance, money): # 잔액과 금액을 인자로 받음
    print("입금이 완료되었습니다. 잔액은 {}원 입니다.". format(balance + money))
    return balance + money # 새로운 잔액을 반환함

balance = 0
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {}원 입니다.". format(balance - money))
        return balance - money
    else:
        print("출금할 수 없습니다. 잔액은 {}원 입니다.". format(balance))
        return balance

balance = 0
balance = deposit(balance, 5000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)

def withdraw_night(balance, money): # 수수료가 생기는 경우
    commission = 100
    return commission, balance - money - commission

commission, balance = withdraw_night(balance, 500) # commission, balance 변수를 withdraw_night 함수를 통해 초기화
print("수수료 {}원, 잔액은 {}원 입니다.". format(commission,balance))


# def profile(name, age, main_lang):
#     print ("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}". \
#         format(name, age, main_lang)) #이렇게 역슬러시를 하고 엔터로 띄워쓰면 한줄로 인식한다.
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "C++")

# 함수의 기본값 설정법 : 파라미터를 전달받지 않았을때 들어갈 값 설정하기.
def profile(name, age = 17, main_lang = "파이썬"):
    print ("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}". \
        format(name, age, main_lang)) #이렇게 역슬러시를 하고 엔터로 띄워쓰면 한줄로 인식한다.
profile("유재석")
profile("김태호", 20)

# 키워드값을 이용한 함수 호출 특정 항목 = ""로 초기화하면 순서가 뒤죽박죽이여도 호출이 가능하다
profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "C++", name = "조세호")
profile("이건우", 24, "파이썬..?") # 키워드값을 넣지 않으면 그냥 순서대로 초기화됨.

# 가변 인자 : *이름 으로 생성
def profile2(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {}\t나이 : {}\t". format(name, age), end = "") # ,end = ""로 끝내면, print후 줄바꿈을 하지 않고 이어서 써진다.
    print(lang1, lang2, lang3, lang4, lang5)

profile2("유재석", 20, "Python", "Java", "C++", "Swift", "C#") # 만약 할줄 아는 언어가 더 많다면? 함수 자체를 바꿔야함.
profile2("김태호", 25, "Kotlin", "C", "", "", "") # 이렇게 만약에 할 수 있는 언어가 적다면 매번 빈칸을 만들어야함. ==> 가변인자 사용 

def profile3(name, age, *language): # 가변인자 *language
    print("이름 : {}\t나이 : {}\t". format(name, age), end = "")
    for lang in language: # for문을 통해서 print
        print(lang, end = " ")
    print()
profile3("이건우", 24, "Python", "C", "C++", "Swift", "Java", "Javascript") # 개수에 상관없이 입력 가능


# 지역변수와 전역변수 : 함수 내에서는 이름이 같더라도 전역변수를 그냥 쓸 수는 없다. 인자로 받지 않는 한! 
gun = 10 #전역변수
def check(soldiers):
    gun = 20 # 지역변수
    gun = gun - soldiers
    print("(지역)함수 내 : {}". format(gun))

def check2(soldiers):
    global gun # 전역공간에 있는 gun 변수를 사용하겠다는 선언
    gun = gun - soldiers
    print("(전역)함수 내 : {}". format(gun))

def check3(gun, soldiers):
    gun = gun - soldiers # 이렇게 하면 인자로 받아서 함수 내의 지역변수로 이용하지만 밖의 gun값이 바뀌진 않는다.
    print("(인수, 변환)함수 내 : {}". format(gun))
    return gun # return을 사용하면 함수 내의 지역변수로 바뀐 gun의 값을 전역변수 gun의 값에 넣을 수 있다.

check(2)
print("함수 밖 : {}". format(gun)) # 함수 밖의 값은 변하지 않았다.
check2(2)
print("함수 밖 : {}". format(gun)) # global 선언으로 gun을 사용하면 함수 밖의 변수 gun의 값도 바뀐다.
gun = check3(gun, 2)
print("함수 밖 : {}". format(gun))