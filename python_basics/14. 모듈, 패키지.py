# 모듈

import theater_module # theater_module파일에 따로 정의해놓은 모듈을 import로 불러와서 사용이 가능하다.
theater_module. price(3)
theater_module. price_discount(4)
theater_module. price_soldier(4)
print(theater_module.l)
import theater_module as mv # as ~~로 별명을 붙여 사용 가능
mv.price(5)

from theater_module import * # 이렇게 쓰면 theater_module. 부분 필요 없이 그냥 쓸 수 있다.
price(10)
price_discount(11)
price_soldier(2)

from theater_module import price, price_soldier # 이렇게 쓰면 일부의 함수만 import해서 사용이 가능하다.
price(1)
price_soldier(2)

# 패키지 : 모듈을 모아놓은 집합 - new folder -> travel 만듬

import travel.thailand # travel 패키지 밑의 thailand 모듈을 호출
trip_to = travel.thailand.ThailandPackage() #ThailandPackage클래스를 호출하여 trip_to 객체를 초기화
trip_to. detail() # 객체의 detail부분 호출

from travel import vietnam
trip_to = vietnam. VietnamPackage()
trip_to. detail()

# __all__
# travel. __init__모듈에 아무것도 없는 상태에서는 from travel import * 로 모두 호출한다하면 에러가 뜬다.
# 이는 패키지에서 모듈의 공개범위를 설정하지 않았기 때문인데, 이는 __all__구문으로 설정이 가능하다.

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to. detail() # 설정 후에는 잘 되는 모습

# trip_to = thailand.ThailandPackage() # 얘는 에러 (vietnam까지만 공개됨)

# 패키지, 모듈의 위치를 확인하는 법 : inspect
import inspect # 확인하게 해주는 애
import random
print(inspect. getfile(random)) # inspect. getfile(모듈/패키지 이름) 하면 위치를 알려줌
print(inspect. getfile(vietnam))