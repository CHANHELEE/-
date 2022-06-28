from numpy import float16
import pandas as pd 
import openpyxl
import os
import glob

for k in range(2004,2022): # 각각의 년도에 대한 모든 리뷰를 하나의 리뷰로 합침.
    path = f"/Users/lee/Desktop/리뷰/{k}"
    li=os.listdir(path)
    try:
        li.remove('.DS_Store')
    except:
        pass

    excel = pd.DataFrame()
    for i in range(0,len(li)):
        df = pd.read_excel(f"/Users/lee/Desktop/리뷰/{k}/{li[i].replace('~$','')}",engine='openpyxl')
        excel = excel.append(df, ignore_index=True)
    
    excel.to_excel(f'/Users/lee/Desktop/리뷰 통합본/{k}통합본.xlsx',index=False)

    if(k==2016 or k==2019): # 용량이 커서 파일이 2개로 나뉘어진 년도에대해 한번더 for문 실행.
        path = f"/Users/lee/Desktop/{k}"
        li=os.listdir(path)
        try:
            li.remove('.DS_Store')
        except:
            pass
        
        excel = pd.DataFrame()
        for i in range(0,len(li)):
            df = pd.read_excel(f"/Users/lee/Desktop/{k}/{li[i].replace('~$','')}",engine='openpyxl')
            excel = excel.append(df, ignore_index=True)
        excel.to_excel(f'/Users/lee/Desktop/리뷰 통합본/{k}통합본2.xlsx',index=False)


