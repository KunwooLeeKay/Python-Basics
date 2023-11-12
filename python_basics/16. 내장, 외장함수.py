# 내장 함수 : input, dir 등등
# 외장 함수 : import로 사용하는 함수 (ex. random)

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시하는 내장함수
print(dir())
import random
print(dir())
import pickle
print(dir())
# print(dir(random))

lst = [1,2,3]
print(dir(lst)) # 리스트에서 사용할 수 있는 명령어 리스트

name = "Jim"
print(dir(name)) # 문자열에서 사용할 수 있는 명령어 리스트

# 또는 구글에서 list of pthon builtins 검색

# 외장함수 : 구글에서 list of python modules 검색
# 예시
# glob : 경로 내의 폴더 / 파일 목록 조회 (dir과 유사)
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일 출력

# os : 운영체제에서 제공하는 기본 기능
import os
print(os. getcwd()) # 현재 디렉토리 표시
folder = "sample_dir"
if os.path.exists(folder): # os.path.exists(폴더이름) : 존재여부를 알 수 있는 구문
    print("이미 존재하는 폴더입니다.")
    os. rmdir(folder) # os.rmdir(폴더이름) : 폴더 삭제
    print(folder, "폴더를 삭제하였습니다. ")
else:
    os. makedirs(folder) # os. makedirs(폴더이름) : 폴더 생성
    print(folder, "폴더를 생성하였습니다.")
print(os. listdir()) # glob과 유사한 기능 - 폴더 리스트

# time : 시간 관련 함수들
import time
print(dir(time))
print(time. localtime())
print(time. strftime("%Y-%m-%d %H:%M:%S")) # 이렇게 적으면 연-월-일 시:분:초 를 쓸 수 있다.(strftime)

# datetime : 날짜 관련 함수들
import datetime
print("오늘 날짜는", datetime.date.today(), "입니다") # datetime.date.today : 오늘 날짜
today = datetime.date.today()
td = datetime. timedelta(days = 100) # 100일 저장
print("100일 뒤 날짜는", today + td)


##=====##=====##=====##=====##=====##=====##=====##=====##=====##=====##=====##=====

# 숫자처리 함수
print(abs(-5)) # 절대값 : abs
print(pow(4,2)) # 거듭제곱(밑, 지수)
print(max(5,10,1000,123)) #최대값. min도 됨
print(round(3.141592)) # 반올림
print(round(5.989)) 
from math import * # 올림, 제곱근, 내림 등 사용 가능

# 랜덤 함수
from random import * # random 라이브러리의 모든 것을 사용한다는 뜻
print(random()) #0.0 ~ 9.0 임의의 값 생성
print(random()*10) # 0.0 ~ 9.0 임의의 값 생성
print(int(random()*10)) # 0 ~ 9 임의의 값 생성
print(int(random()*10 +1)) # 1 ~ 10 임의의 값 생성

print(int(random()*100+1)) # 1 ~ 100 임의의 값 생성
print(randrange(1,101)) # 1 이상 101 미만의 임의의 값 생성
print(randint(1,100)) # 1 이상 100 이하의 임의의 값 생성

# 랜덤 모듈의 리스트 셔플, 샘플

lst = [1,2,3,4,5]
print(lst)
shuffle(lst) # 리스트 내의 순서를 랜덤으로 섞어줌
print(lst)
print(sample(lst,1)) # 리스트 내에서 두번째 인수의 수만큼 랜덤으로 숫자를 뽑아줌