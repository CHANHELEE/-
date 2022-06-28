import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


for i in range(1,19): ## (2)~(5)과정을 반복하기 위한 for문
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(3)
    url = "https://www.kobis.or.kr/kobis/business/stat/boxs/findYearlyBoxOfficeList.do"
    driver.get(url)
    driver.implicitly_wait(3)
    nm=[] #(5)번 과정에서 4개의 각각 다른 리스트들의 인덱스를 하나의 인덱스로 만들어 줄 list
    name=[] #영화명List
    people=[] #관객수 list
    driver.find_element_by_xpath(f'//*[@id="sSearchYearFrom"]/option[{i}]').click()
    driver.implicitly_wait(3)
    driver.find_element_by_css_selector('#searchForm > div > div.wrap_btn > button').click()
    driver.implicitly_wait(3)
 
    i=i+2003
    
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    
    k=soup.find_all("td",id="td_movie")
    for j in k:
    
        k2 = j.get_text().strip()
        k3 = k2.replace(',','')
        name.append(k3)
    q=soup.find_all("td",id='td_audiAcc')
    for p in q:
        q2 = p.get_text().strip()
        q3 = q2.replace(',','')

        q4=int(q3)
        people.append(q4)
    driver.quit()
    #전략 1-(1)~ 1-(3)에 해당되는 소스코드
#--------------------------------------------------------------------
    genli=[]
    conli=[]
    for p in range(0, len(name)):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(3)
        url = "https://movie.naver.com/"
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="ipt_tx_srch"]').click()
        driver.implicitly_wait(10)
        element=driver.find_element_by_xpath('//*[@id="ipt_tx_srch"]')
        driver.implicitly_wait(10)
        element.send_keys(name[p], Keys.ENTER)
        driver.implicitly_wait(10)
        url2=driver.current_url
        r=requests.get(url2)
        html=r.text
        soup=BeautifulSoup(html,'html.parser')
        g=soup.select('ul.search_list_1>li>dl>dd.etc')[0]
        g2=g.get_text().strip()
        g3=g2.split('|')
        print(g3)
        genre=g3[0].strip()
        genre2=genre.split(',')
        genre3=genre2[0]
        county=g3[1].strip()
        print(genre3)
        print(county)
        
        genli.append(genre3.replace(',',''))
        conli.append(county.replace(',',''))
        driver.quit()

        #전략 1-(4)에 해당되는 소스코드
#-------------------------------------------------------------

        

    for v in range(0,len(name)):
        nm.append([name[v],people[v],genli[v],conli[v]])
    columns = ['Movie', 'Count','Genre','Country']

    mData = pd.DataFrame(nm, columns = columns)

    mData.to_excel(f'/Users/lee/Desktop/영화정보/{i}.xlsx',index=False ,engine='xlsxwriter')
    #전략 1-(5)에 해당되는 소스코드
#---------------------------------------------------------------
    
    
    