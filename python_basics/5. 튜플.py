# 튜플 : 내용 변경, 추가를 할 수 없는 리스트. 대신 속도가 빠름
menu = ("돈까스", "치즈까스") # ( , ) 형식으로 선언
print(menu[0])
# menu.add("생선까스") : 불가
(name, age, hobby) = ("김종국", 20, "코딩") # 괄호 안쳐도 가능
print(name, age)

# 세트(집합) : 중복이 안되고 순서가 없는 것
my_set = {1,2,3,3,3}
print(my_set) # 3이 한번만 출력됨
print("=======")
my_list = list(my_set)
print(my_list[1])
print("=======")


java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 이런식으로 선언도 가능
c_lan = list([1,2,3])
javascript = dict({1:2, 3:4, 4:5})
swift = tuple((1,2,3))  # list, dict, tuple 도 다 된다.

# java와 python의 교집합 
print(java & python)
print(java. intersection(python))

# java와 python의 합집합
print(java | python)
print(java. union(python))

# java와 python의 차집합(java는 가능하나 python은 못하는 개발자)
print(java - python)
print(java. difference(python))

# 항목 추가. add
python.add("김태호")
print(python)

# 항목 제거. remove
java.remove("김태호")
print(java)


# 자료 구조의 변경
menu = {"커피", "주스", "우유"} # set
print(menu, type(menu))
menu = list(menu) # list형으로 변경
print(menu, type(menu))
menu = tuple(menu) # tuple형으로 변경
print(menu, type(menu))


