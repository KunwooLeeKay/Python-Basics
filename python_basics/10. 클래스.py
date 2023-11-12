# Class : 하나의 틀 - 연관이 있는 변수와 함수의 집합

# self 를 붙이면 클래스 내에 있는 내용이라는 것이고, 붙이지 않으면 인수로 받은 내용을 가리킨다.
# 꼭 self라고 해야하는건 아니지만 관습적으로 self를 사용한다.
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.". format(self. name))
        print("체력 {}, 공격력 {}". format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # marine1이라는 객체가 생성된다.
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# __init__함수 : 파이썬의 생성자.
# 객체 : Class로부터 만들어지는 애들 = marine1, marine2, tank. 또는 Unit 클래스의 인스턴스라고도 부름

# 멤버 변수 : 클래스 내에서 정의된 변수 : '.'
# 멤버 변수를 이용하면 특정 개체의 원하는 특정 속성을 가져올 수 있다.
print("유닛 이름 : {}, 공격력 : {}". format(marine1. name, marine1. damage))

# 클래스 외부에서 객체에 변수 추가할당(외부에서)
marine2. steampack = True 
marine2. isflyable = 0
# 클래스에 없던 steampack 변수를 추가로 할당함. 이렇게하면 marine2에만 steampack이라는 멤버가 확장됨(기존변수는 변화 x)
if(marine2. steampack ==True):
    print("{}의 공격력이 크게 상승했습니다. ". format(marine2.name))

if(marine2. isflyable == 0):
    print("{}유닛은 날 수 없습니다.". format(marine2. name))

# 메소드
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.". format(self. name))
        print("체력 {}, 공격력 {}". format(self.hp, self.damage))

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 : {}]". format\
            (self.name, location, self.damage)) 
                # self를 붙여서 쓰면 자신의 클래스 내의 변수를 사용, 안붙이면 전달받은 인자의 값을 쓴다.

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.". format(self.name, damage))
        self. hp -= damage
        print("{} : 현재 체력은 {}입니다. ".  format(self.name, self.hp))
        if self.hp <=0:
            print("{} : 파괴되었습니다.". format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16) # def __init__에 파이어뱃의 정보 입력
firebat1. attack("5시") # attack 함수에 location정보 전달
firebat1. damaged(25) # damaged 함수에 25의 데미지 정보 전달
firebat1. damaged(25)