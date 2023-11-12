# 파일 입출력
# 파일 열기: open("파일명", "덮어쓰기 = w", encoding = "") 인코딩 안하면 한글 안됨
score_file = open("score.txt", "w", encoding = "utf8") 
print("수학 : 0", file = score_file) # print를 사용해 파일에 작성
print("영어 : 50", file = score_file)
score_file. close()

score_file = open("score.txt", "a", encoding = "utf8") # 추가하기 : "a"
score_file.write("과학 : 80") # write를 이용해 작성
score_file.write("\n코딩 : 100")
score_file. close()

# 전체 파일 읽기
read_score = open("score.txt", "r", encoding = "utf8") 
print(read_score.read())
print("===============")

# 한줄씩 읽기 : 한줄 읽고 커서를 다음으로 옮김.
read_score.seek(0) # seek으로 0번째 바이트로 이동(처음으로 커서이동)
print(read_score.readline())
print(read_score.readline())
print(read_score.readline())
print(read_score.readline())
read_score.seek(0)
read_score.close()
print("===============")

# 몇줄인지 모를 때 다 출력하는 법
read_unknown = open("score.txt", "r", encoding = "utf8")
while True:
    line = read_unknown.readline()
    print(line)
    if not line: # if not line : line이 비어있다면 break
        break
read_unknown.seek(0)
read_unknown.close()
print("===============")

# 파일을 리스트의 형태로 저장하는 법
read_list = open("score.txt", "r", encoding = "utf8")
lines = read_list.readlines() # readlines()를 통해 lines 리스트에 모든 줄을 넣어줌
for line in lines:
    print(line)
read_list.close()

# Pickle : 프로그램상의 데이터를 파일 형태로 저장하는 것

import pickle
profile_file = open("profile.pickle", "wb") # 피클에서 쓰기 위해선 wb(쓰기 + 바이너리)로 해야하며, 인코딩을 할 필요는 없음
profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장(pickle.dump 이용) -> profile에 있는 정보를 profile_file에 저장

profile_file.close()

read_file = open("profile.pickle", "rb")
profile = pickle.load(read_file) # pickle파일에 있는 정보를 profile에 불러오기.
print(profile)
read_file. close()

# with : open, close의 과정 없이 파일에 엑세스할 수 있다
import pickle

with open("profile.pickle", "rb") as profile_with: # profile.pickle 파일을 읽기로 읽어서 profile_with변수에 저장
    print(pickle.load(profile_with)) # pickle.load를 사용해 profile_with에 있는 값을 print한다

# with 활용

with open("study.txt", "w", encoding = "utf8") as study_file: 
    # with 안에서 sudy.text 파일을 쓰기형식으로 만들고 study_file변수에 저장
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding = "utf8") as study_file:
    print(study_file. read())

