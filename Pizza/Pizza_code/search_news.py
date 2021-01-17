import os, re, usecsv
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")

# 최다 조회수 자료
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

for index, c in enumerate(max_match.values):
    print("="*50)
    print(f"브랜드명: {brand[index]}")
    print(f"최다조회수 날짜: {df.iloc[c, 0]}")
    print(f"{round(df.iloc[c, index+1], 2)}점")
    print("")

browser = webdriver.Chrome("C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Python/webscraping_basic/chromedriver.exe")

#1. 네이버 이동
browser.get("http://naver.com")

#2. 브랜드명 검색
elem = browser.find_element_by_id("query")
elem.click()
elem.send_keys("피자헛")
elem.send_keys(Keys.ENTER)
time.sleep(2)

#3. 브랜드 검색 옵션 설정
elem = browser.find_element_by_id("search_option_button")
elem.click()

elem = browser.find_element_by_id("_nx_search_option_date_link")
elem.click()
time.sleep(2)
elem = browser.find_element_by_xpath("//*[@id='_nx_date_from']")
print(elem)
elem.click()
time.sleep(2)
elem.send_keys("2020.12.11")
time.sleep(2)
elem = browser.find_element_by_xpath("//*[@id='_nx_date_to']")
elem.click()
time.sleep(2)
elem.send_keys("2020.12.15")
time.sleep(2)
elem = browser.find_element_by_class_name("_btn_submit_")
elem.click()

# next step
# 뉴스 탭에 들어가서 상위 뉴스 5개 제목과 링크 가져오기

# #(selenium 기능 학습)
# browser.back()
# browser.forward()
# browser.refresh()
# elem = browser.find_element_by_id("query")

# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_tag_name("a") ( 하나만 )
# elem = browser.find_elements_by_tag_name("a") ( 모두다 )
# for e in elem:
#     e.get_attribute("href")
# browser.get("http://daum.net")
# elem = browser.find_element_by_name("q")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
# elem.click()
# browser.quit() #아예 꺼버리기
# browser.close() #탭만 닫아버리기
# # # 터미널에 위와 동일 내용 입력


#3. id, password 입력


# url = "https://news.daum.net/"
# res = requests.get(url)
# res.raise_for_status()

# soup = bs(res.text, 'lxml')
# # title = soup.find_all("div", attrs={"class": "item_issue"})
# #print(title[0].get_text())

# # for i in title:
# #     print(i.get_text().strip(), i.find_all('a')[0].get('href'))

# os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
# f = open("links.txt", 'w')
# for i in soup.find_all('div', {"class": "item_issue"}):
#     f.write(i.find_all('a')[0].get('href') + '\n')

# f.close()

# article = "https://news.v.daum.net/v/20210106171745306"
# soup = bs(ur.urlopen(article).read(), 'html.parser')
# f = open('article1.txt', 'w')
# for i in soup.find_all('p'):
#     f.write(i.text)
# f.close()

# # soup 부분에서 res.text보다  ur.urlopen(링크), 'html.parser' 방식이 더 긁어오는게 많은 것 같음!
# url = "https://news.daum.net/"
# soup = bs(ur.urlopen(url).read(), 'html.parser')
# f = open('article_total.txt', 'w')
# for i in soup.find_all('div', {'class': "item_issue"}):
#     try:
#         f.write(i.text + '\n')
#         f.write(i.find_all('a')[0].get('href') + '\n')
#         soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
#         for j in soup2.find_all('p'):
#             f.write(j.text)
#     except:
#         pass

# f.close()