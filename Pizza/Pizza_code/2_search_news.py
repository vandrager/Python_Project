import os, re, usecsv
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")

# 최다 조회수 자료 데이터 전처러
df = round(pd.read_excel("daily_search.xlsx"), 3)
brand = ['피자헛', '파파존스', '도미노피자', '반올림피자샵', '미스터피자', '피자마루', '피자알볼로', '피자나라치킨공주', '7번가피자', '피자헤븐']
df['날짜'] = df['날짜'].astype('str') # 문자열 메소드 사용을 위해 자료형 변경
dates = df['날짜'].str.split('-') # 문자열을 split 메소드로 분리

df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)

max_match = df.loc[:, "피자헛":"피자헤븐"].idxmax()
print(max_match.keys())
print(max_match.values)

file_brand = []
file_dates = []
for index, c in enumerate(max_match.values):
    print("="*50)
    print(f"브랜드명: {brand[index]}")
    print(f"최다조회수 날짜: {df.iloc[c, 0]}")
    print(f"{round(df.iloc[c, index+1], 2)}점")
    file_brand.append(brand[index])
    file_dates.append(df.iloc[c, 0])
print("")
file = pd.Series(file_dates, index=file_brand, name="date")
file_pd = pd.DataFrame(file)

dates = file_pd['date'].str.split('-') # 문자열을 split 메소드로 분리

file_pd['연'] = dates.str.get(0)
file_pd['월'] = dates.str.get(1)
file_pd['일'] = dates.str.get(2)
print(file_pd['일'][3])
file_pd['best_day'] = 0
file_pd['best_day'] = file_pd['best_day'].astype('str') # 문자열 메소드 사용을 위해 자료형 변경
for i in range(10):
    file_pd['best_day'][i] = "{}.{}.{}".format(file_pd['연'][i], file_pd['월'][i], file_pd['일'][i])

file_pd.drop(['date','연', '월', '일'], axis=1, inplace=True)
print(file_pd)
file_pd.to_excel("dates.xlsx",  encoding= "cp949")
print(file_pd['best_day'][0])
print(file_pd.index[0])

f = open("isseu_data.txt", "w", newline="")
browser = webdriver.Chrome("C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Python/webscraping_basic/chromedriver.exe")


for i in range(10):
    #1. 네이버 이동
    browser.get("http://naver.com")

    #2. 브랜드명 검색
    elem = browser.find_element_by_id("query")
    elem.click()
    elem.send_keys(file_pd.index[i]) # 브랜드 이름도 자동화
    elem.send_keys(Keys.ENTER)
    time.sleep(2)

    #3. 브랜드 검색 옵션 설정
    
    if i == 0:
        elem = browser.find_element_by_id("search_option_button")
        elem.click()
        time.sleep(2)
        
    else:
        pass
    elem = browser.find_element_by_id("_nx_search_option_date_link")
    elem.click()
    time.sleep(2)

    elem = browser.find_element_by_xpath("//*[@id='_nx_date_from']")
    print(elem)
    elem.click()
    time.sleep(2)
    elem.send_keys(file_pd['best_day'][i]) # 날짜 -2 입력
    time.sleep(2)
    elem = browser.find_element_by_xpath("//*[@id='_nx_date_to']")
    time.sleep(2)
    elem.click()
    elem.send_keys(file_pd['best_day'][i]) # 날짜 + 3 입력
    elem = browser.find_element_by_class_name("_btn_submit_")
    elem.click()
    time.sleep(2)
    # 셀레니움 텍스트 찾기
    elem =  browser.find_element_by_partial_link_text("뉴스") # 검색결과 페이지에서 특정 문자열을 포함하는 링크 텍스트 찾기 
    elem.click()
    soup = bs(browser.page_source, "lxml")
    news_list = soup.find_all("div", attrs={"class": "news_area"})
    f.write(file_pd.index[i] + '\n')
    f.write("최다 조회수 일자: {}".format(file_pd['best_day'][i])+ '\n')

    for news in news_list:
        title = news.find("a", attrs={"class":"news_tit"})["title"]
        link = news.find("a", attrs={"class":"news_tit"})["href"]
        print("-"*40)
        print(f"제목 : {title}")
        print(f"링크 : {link}")
        f.write(title+ '\n')
        f.write(link+ '\n')
    f.write('\n')
browser.quit()

f.close()