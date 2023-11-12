from openpyxl import Workbook

wb = Workbook() # 새 워크북을 생성 : 엑셀 파일을 생성함
ws = wb.active # 현재 활성화된 sheet를 가져옴 -> ws에 저장

ws.title = "KunwooSheet" # sheet의 이름을 변경
wb.save("sample.xlsx")
wb.close()