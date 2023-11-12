# 예외처리 : try, except

try:
    print("나누기 전용 계산기!!")
    nums = []
    nums.append(int(input("첫번쨰 숫자를 입력하세요 : ")))
    nums.append(int(input("두번쨰 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{} / {} = {}". format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 숫자를 입력해주세요!")
except ZeroDivisionError as err:
    print("0으로 나눌 수 없습니다!")
    print(err)
except Exception as err: # 그 외 에러 처리기
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)


# 의도적 에러 발생 : raise - 필요할 때 의도적으로 에러를 발생시켜서 except부분으로 오게 할 수 있음.

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = 10
    num2 = 9
    if num1 >=10 or num2 >=10:
        raise ValueError
    print("{} / {} = {}". format(num1, num2, int(num1/num2)))
except ValueError:
    print("한자리 숫자만 입력해주세요!") 

# 사용자 정의 예외처리 : 파이썬에서 정의하고있지 않은 에러를 직접 정의해서 쓰는 것

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = 10
    num2 = 9
    if num1 >=10 or num2 >=10:
        raise BigNumberError("입력값 : {}, {}". format(num1, num2)) # 이렇게 넣어서 BigNumberError속의 에러내용을 정의 가능
    print("{} / {} = {}". format(num1, num2, int(num1/num2)))
except BigNumberError as err:
    print("한자리 숫자만 입력해주세요!") 
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.") #finally구문을 이용하면 에러가 발생하든 잘 돌아가든 출력되는 구문을 만들 수 있음.