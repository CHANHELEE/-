
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
import pandas as pd
import math
from webdriver_manager.chrome import ChromeDriverManager

class review:
    def __init__(self):
        self.current_url=None
        self.tc5=0
    def review_collector(self,x,y):
        for n in range(0,len(x)):
            driver=webdriver.Chrome(ChromeDriverManager().install())
            driver.implicitly_wait(3) 
            url = "https://movie.naver.com/"
            driver.get(url)
            driver.implicitly_wait(10)
            driver.find_element_by_xpath('//*[@id="ipt_tx_srch"]').click()#검색탭 클릭
            driver.implicitly_wait(10)
            element=driver.find_element_by_xpath('//*[@id="ipt_tx_srch"]')
            driver.implicitly_wait(10)
            if (x[n]=="알라딘"):
                element.send_keys("알라딘 2019", Keys.ENTER)
            
            elif(x[n]=="인턴"):
                element.send_keys(x[n]+" 앤 해서웨이", Keys.ENTER)
          
            elif(x[n]=="주먹이 운다(Crying Fist)"):
                element.send_keys("주먹이 운다", Keys.ENTER)
            elif(x[n]=="샤크"):
                element.send_keys("샤크 2004", Keys.ENTER)

            elif(x[n]=="더 박스"):
                element.send_keys("더 박스 조달환", Keys.ENTER)

            elif(x[n]=="007 노 타임 투 다이"):
                element.send_keys("007", Keys.ENTER)
                
            elif(x[n]=="다이 하드 4 : 죽어도 산다"):
                element.send_keys("다이 하드4.0", Keys.ENTER)
            elif(x[n]=="모가디슈" or x[n]=="#살아있다" or x[n]=="터널" or x[n]=="미나리" or x[n]=="기적" or x[n]=="서복"or x[n]=="자산어보" or x[n]=="노바디" or x[n]=="랑종" or x[n]=="극장판 포켓몬스터: 정글의 아이, 코코" or x[n]=="고장난 론" or x[n]=="오션스 써틴" or x[n]=="예스맨" or x[n]=="하울의 움직이는 성" or x[n]=="아바타" or x[n]=="아이들..." or "해무" in x[n] or "내부자들" in x[n] or x[n]=="데드풀" or x[n]=="신비한 동물사전") :
                element.send_keys(x[n], Keys.ENTER)
            elif(x[n]=="비긴 어게인"):
                element.send_keys(x[n], Keys.ENTER) 
            else:
                element.send_keys(x[n]+" "+str(y), Keys.ENTER) 
                
            driver.implicitly_wait(10)
            #전략 2의 (1)-1 과정
            #------------------------------------------
            url2=driver.current_url
            r=requests.get(url2)
            html=r.text

            soup=BeautifulSoup(html,'html.parser')
            mn=soup.select('tr.text')[0]
            li4=[]
            for i in mn:
                li4.append(i.text)
                for j in range(0,len(li4)):
                    if li4[j]=='\n':
                        del li4[j]
            #이미지 파일을 비교하기 위해 리스트에 해당 이미지에 달린 title을 넣어줌.
            #전략 2의 (1)-2 과정
#------------------------------------------------------------------------------
            flag=0#이미지를 선택할지 동영상을 선택할지 구분하기 위한 flag
            if flag==0:
                for k in range(0,5):
                    print(li4[k].replace(" ",""),x[n].replace(" ",""))
                    if (li4[k].replace(" ","")==x[n].replace(" ","")):
                        time.sleep(1)    
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[2]/td[{k+1}]/a')))
                        driver.find_element_by_xpath(f'//*[@id="old_content"]/table/tbody/tr[2]/td[{k+1}]/a').click()
                        driver.implicitly_wait(10)
                        break
                    else:
                        if(k==4):
                            flag=1
                        print(flag)
                        
            
            if flag==1:
                driver.find_element_by_xpath('//*[@id="old_content"]/ul[2]/li/dl/dt/a').click() #이미지 탭 클릭

            #전략 2의 (1)-2 과정    
#-------------------------------------------------------------------------------------
            time.sleep(1)      
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="movieEndTabMenu"]/li[5]/a/em')))                 
            driver.find_element_by_xpath('//*[@id="movieEndTabMenu"]/li[5]/a/em').click() #평점 탭 클릭  
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="movieEndTabMenu"]/li[5]/a/em')))
            driver.implicitly_wait(20)
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pointAfterListIframe"]')))
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="pointAfterListIframe"]')))
            driver.implicitly_wait(10)
            
            driver.find_element_by_xpath('//*[@id="orderCheckbox"]/ul[1]/li[3]/a').click()          
            driver.implicitly_wait(10) 
            
                
            html=driver.page_source
            driver.implicitly_wait(10)
            soup=BeautifulSoup(html,'html.parser')
            tc=soup.select_one("strong.total>em") #tc = total review count 
            tc2 =tc.get_text().strip()
            tc3 = int(tc2.replace(',',''))
            tc4 = math.ceil(tc3/10)
            
            result_d =[]
            score_d=[]
            review_d =[]
            for i in range(1,tc4+1):
        #---------------------------------------------------
        #전략 2의 (1)-4과정

                if i==2000: #page가 2000을 넘었을 때.
                    for v in range(0,len(score_d)):
                        result_d.append([score_d[v],review_d[v]])
                    columns = ['score', 'review']
                    kData = pd.DataFrame(result_d, columns = columns)
                    y= int(y)
                    kData.to_excel(f'/Users/lee/Desktop/년도별 리뷰파일/{y}/{x[n]}.xlsx',index=False)
                    y=str(y)
                    self.tc5=tc4-i
                    self.current_url=driver.current_url
                    driver.implicitly_wait(9999)
                    self.review_colletor2(x[n],y)
                    driver.quit()
                    break
    #------------------------------------------------------------------------------------------------
        #전략 2의 1-(3) 과정
                driver.implicitly_wait(3)
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="pagerTagAnchor{i}"]')))
                driver.find_element_by_xpath(f'//*[@id="pagerTagAnchor{i}"]').click()
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="pagerTagAnchor{i}"]')))
                driver.implicitly_wait(3)
                
                
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                score=soup.select('div.star_score> em')
                
                
                for j in score: #평점을 뽑아내기 위한 for문
                        origin = j.get_text().strip()
                        or2=int(origin) 
                        score_d.append(or2)
                for k in range(0,len(score)): #리뷰를 뽑아내기위한 for 문
                        review=soup.select_one(f'span#_filtered_ment_{k}')
                        review2 = review.get_text().strip()
                        review_d.append(review2)
                for j in range(0,len(review_d)):
                        review_d[j]=review_d[j].replace(',','')
                        
                      
            for v in range(0,len(score_d)):
                    result_d.append([score_d[v],review_d[v]])                  
            columns = ['score', 'review']
            mData = pd.DataFrame(result_d, columns = columns)
            y= int(y)
            
            mData.to_excel(f'/Users/lee/Desktop/년도별 리뷰파일/{y}/{x[n]}.xlsx',index=False)
            driver.quit()
#-------------------------------------------------------------------------------------------------

#page가 2000을 넘었을 때 다시 호출할 함수.
    def review_colletor2(self,x,y):
     
            driver=webdriver.Chrome(ChromeDriverManager().install())
            driver.implicitly_wait(3) 
            url = self.current_url
            driver.get(url)
            driver.implicitly_wait(3)
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="pointAfterListIframe"]')))
            driver.implicitly_wait(10)
            driver.find_element_by_xpath('//*[@id="orderCheckbox"]/ul[1]/li[4]/a').click()        
            driver.implicitly_wait(10) 

            html=driver.page_source
            driver.implicitly_wait(10)
            soup=BeautifulSoup(html,'html.parser')
            tc=soup.select_one("strong.total>em") #tc = total review count
            tc2 =tc.get_text().strip()
            tc3 = int(tc2.replace(',',''))
            tc4 = math.ceil(tc3/10)
            
            result_d =[]
            score_d=[]
            review_d =[]
            
            for i in range(1,2000):
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="pagerTagAnchor{i}"]')))
                driver.find_element_by_xpath(f'//*[@id="pagerTagAnchor{i}"]').click()
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="pagerTagAnchor{i}"]')))
                driver.implicitly_wait(10)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                score=soup.select('div.star_score> em')
                
                
                for j in score:
                        origin = j.get_text().strip()
                        or2=int(origin) 
                        score_d.append(or2)
                for k in range(0,len(score)):
                        review=soup.select_one(f'span#_filtered_ment_{k}')
                        review2 = review.get_text().strip()
                        review_d.append(review2)
                for j in range(0,len(review_d)):
                        review_d[j]=review_d[j].replace(',','')
                      
            for v in range(0,len(score_d)):
                    result_d.append([score_d[v],review_d[v]])                  
            columns = ['score', 'review']
            mData = pd.DataFrame(result_d, columns = columns)
            y= int(y)
            
            mData.to_excel(f'/Users/lee/Desktop/년도별 리뷰파일/{y}/{x}추가분.xlsx',index=False)
            return driver.quit()
