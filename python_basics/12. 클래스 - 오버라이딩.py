# 메소드 오버라이딩 : 자식으로부터 부모클래스에 상속 = 오버로딩이라고 부름(역상속(?))

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 : {}]". format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # 클래스를 선언할 때 이름 뒤에 이름(상속받을 클래스 이름) 으로 하면 상속받을 수 있다
    def __init__(self, name, hp, speed ,damage):
        # self.name = name
        # self.hp = hp : 상속받을 때에는 이 부분을 다시 하지 않고,
        Unit.__init__(self, name, hp, speed) # 이런식으로 상속을 받음
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.". format(self. name))
        print("체력 {}, 공격력 {}". format(self.hp, self.damage))

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 : {}]". format\
            (self.name, location, self.damage)) 
        print("{} : {} 데미지를 입었습니다.". format(self.name, damage))
        self. hp -= self.damage
        print("{} : 현재 체력은 {}입니다. ".  format(self.name, self.hp))
        if self.hp <=0:
            print("{} : 파괴되었습니다.". format(self.name))


# 다중 상속

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self. flying_speed = flying_speed
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 : {}]". format(name, location, self.flying_speed))
# 공중 공격유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit. __init__(self, name, hp,0 , damage) # 지상스피드 = 0
        Flyable. __init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location) # 이 부분이 메소드 오버라이딩!!!!

vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시") # 여기서 문제점 : 지상유닛과 공중유닛을 움직일때 다른 함수를 써야해서 번거로움 -> 오버라이딩
battlecruiser.move("9시")

# pass : 일단 넘어간다는 명령어

def game_start():
    print("게임 시작 ! ")
def game_over():
    pass
game_start()
game_over() # 아무것도 안넣고 pass만 했지만 오류 안나고 아무것도 안하는 모습

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 이런식으로 일단 아무것도 안해놓고 마치 완성된것 처럼 넘어갈 수 있음
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# super : 상속을 다른 방법으로 할 수 있다. 하지만 다중 상속을 할 때에는 사용할 수 없다. 다중으로 하면 앞에 쓴것만 상속된다.
class BuildingUnit2(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0) #원래 하던 상속방식
        super().__init__(name, hp, 0) # super 사용 상속
        self.location = location
