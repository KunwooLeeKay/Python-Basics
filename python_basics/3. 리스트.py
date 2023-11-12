# 리스트[]
subway = [10, 20, 30]

print(subway[:-1])
print([10,20] in subway)
sum(subway)
print(subway.reverse)
print(subway)
subway.reverse()
exit()
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호는 몇 번째 칸에 타고 있는가? index 이용 배열의 순서 구하기
print(subway.index("조세호")+1)
# print(subway.find("유재석")+1) : List에선 find이용 불가

#하하가 다음 정류장에서 다음 칸에 탐. append 이용 배열의 맨 뒤에 하나를 추가하기
subway.append("하하")
subway.append("이건우")
# subway.add("이거 되나?") 안댐ㅎ
print(subway)

#정형돈을 유재석, 조세호 사이에 탐. insert 이용 배열의 중간에 하나를 끼워넣기
subway.insert(1, "정형돈")
subway.insert(4, "건우!")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄. pop이용 배열의 맨 뒤의 값을 빼내기
print(subway.pop()) # print 내에서 pop을 해도 subway 리스트에서 삭제된다
print(subway)

print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인. count를 사용해 셀 수 있음
subway.append("유재석")
print(subway)
print(subway. count("유재석"))

#리스트의 정렬. sort 이용
num_list = [100,32,34,65,2]
num_list.sort()
abc_list = ['a', 'c', 'b'] # 문자도 sort 가능.
abc_list.sort()
print(num_list)
print(abc_list)

#순서 뒤집기. reverse 이용
num_list. reverse()
abc_list. reverse()
print(num_list)
print(abc_list)

#reverse <-> reversed : reversed를 사용하면 실제 리스트를 뒤집진 않고 그냥 임시로 값을 뒤집어서 반환해준다.

#모두 지우기
num_list.clear()
print(num_list)

#리스트는 자료형에 관련없이 섞을 수 있다.
mix_list = ["이건우", 24, True]
# mix_list. sort() : 불가
mix_list. reverse() # reverse 는 가능.
print(mix_list)

#리스트 확장. extend 이용 -> mix_list를 num_list 뒤에 붙여버림
num_list = [100,32,34,65,2]
num_list.extend(mix_list)
print(num_list)
print(mix_list)
num_list. extend(abc_list)
print(num_list)