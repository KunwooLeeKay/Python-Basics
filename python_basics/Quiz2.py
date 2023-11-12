# Quiz) 보고서 파일을 만드는 프로그램

# week = 1
# while week <= 50:
#     with open("{}주차.txt". format(week), "w", encoding = "utf8") as report:
#         report. write("- {} 주차 주간보고 - \n". format(week))
#         report. write("부서 : \n이름 : \n업무 요약 : \n")
#         week += 1 # : while문

# for i in range(1,51): # for문
#     with open(str(i) + "주차.txt", "w", encoding = "utf8") as report_file:
#         report_file.write("- {} 주차 주간보고 - \n". format(i))
#         report_file.write("부서 : \n이름 : \n업무 요약 : \n")

# Quiz) 부동산 프로그램

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self. location = location
        self. house_type = house_type
        self. deal_type = deal_type
        self. price = price
        self. completion_year = completion_year
    # 매물 정보 표시
    def show_detail(self):
        print(self. location, self.house_type, self.deal_type, self.price, self.completion_year)

house = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

house.append(house1)
house.append(house2)
house.append(house3)

print("총 {}대의 매물이 있습니다.". format(len(house)))
for house_no in house:
    house_no.show_detail()
    House.show_detail(house_no)