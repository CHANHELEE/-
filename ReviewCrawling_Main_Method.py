
from review import review
import openpyxl

rev=review()

for k in range(2004,2022): 
    wb=openpyxl.load_workbook(filename=f"/Users/lee/Desktop/영화정보/{k}.xlsx")
    # 2004~2021년도 영화데이터셋 사용
#-------------------------------------------------------------------
    wb.active
    ws=wb['Sheet1']
    li=[]
    li2=[]
    for i in ws['A']:
        li.append(i.value)
    del li[0]
    for j in li :
        li2.append(j)
    #전략 2의 (2)-2 과정
#----------------------------------------
    rev.review_collector(li2,str(k))
    #전략 2의 (2)-3 과정

















    