# 사전{} : 키에 값을 매칭시키는 리스트. 사전[키값]으로 불러올 수 있음

cabinet = {3:"유재석", 100:"조세호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet. get(3)) #get으로 가져올 수도 있음

# 만약 사전에 없는 키값을 입력하면, 대괄호로 된 것은 에러가 뜨며 종료, get으로 된 것은 None이라고 출력된다.
# print(cabinet[1]) : error!
print(cabinet.get(5))
print(cabinet. get(5, "사용가능")) # 이렇게 쓰면 값이 있다면 5번 캐비냇 값을 출력, 없다면 "사용가능"이라고 출력한다
print(cabinet. get(3, "그냥 함 해봄ㅎ"))

# key in 자료이름 하면, 사전 자료형 안에 특정 키값이 있는지 확인할 수 있다.
print(3 in cabinet) # True
print(5 in cabinet) # False
is_occupied = 100 in cabinet
print(is_occupied)

cabinet2 = {"A-3" : "유재석", "B-100" : "조세호"} # 이처럼 숫자가 아닌 것으로도 key값을 입력할 수 있음
print("dsdsdfsdfsfdsdf" + cabinet2. get("A-3"))
print(cabinet2["B-100"])

# 사전에 새로운 값을 추가. 처음 사전을 선언할때처럼 다시 넣으면 마지막 것으로 초기화돼버림
# 추가방법 : 사전이름 ["새로운 키값"] = "새로운 벨류값"
print("===")
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "김태호"
cabinet["ROYAL"] = "이건우"
print(cabinet)

# 사전 내의 값 제거. del
del cabinet["A-3"]
print(cabinet)
del cabinet["ROYAL"]
print(cabinet)

# key들만, value들만 출력 : keys, values
print(cabinet.keys())
print(cabinet.values())

# key, value 쌍으로 출력 : items
print(cabinet. items())
print(cabinet)

# 사전 내의 모든 값 제거 : clear
cabinet.clear()
print(cabinet)