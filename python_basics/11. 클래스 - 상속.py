# 상속
# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 클래스를 선언할 때 이름 뒤에 이름(상속받을 클래스 이름) 으로 하면 상속받을 수 있다
    def __init__(self, name, hp, damage):
        # self.name = name
        # self.hp = hp : 상속받을 때에는 이 부분을 다시 하지 않고,
        Unit.__init__(self, name, hp) # 이런식으로 상속을 받음
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.". format(self. name))
        print("체력 {}, 공격력 {}". format(self.hp, self.damage))

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 : {}]". format\
            (self.name, location, self.damage)) # self를 붙여서 쓰면 자신의 클래스 내의 변수를 사용, 안붙이면 전달받은 인자의 값을 쓴다.

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


# 다중 상속

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self. flying_speed = flying_speed
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 : {}]". format(name, location, self.flying_speed))
# 공중 공격유닛 클래스 : 클래스 AttackUnit과 Flyable의 융합
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit. __init__(self, name, hp, damage)
        Flyable. __init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200,6,5)
valkyrie. fly(valkyrie.name, "3시")