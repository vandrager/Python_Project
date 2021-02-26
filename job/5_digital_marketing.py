import os, requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook
from datetime import datetime
today = datetime.today().strftime("%Y%m%d")

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면")

interval = 2
browser = webdriver.Chrome("C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Python/webscraping_basic/chromedriver.exe")
browser.maximize_window()
time.sleep(interval)
browser.get("http://www.jobkorea.co.kr/recruit/joblist?menucode=duty")

write_wb = Workbook()
write_ws = write_wb.active
write_ws.append(["회사명", "공고명", "기간", "링크"])

# 공고 선택 조건 세팅(마케팅/신입/지역(서울, 경기))
elem = browser.find_element_by_xpath("//*[@id='devSearchForm']/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[2]/label") # 마케팅
elem.click()

elem = browser.find_element_by_xpath("//*[@id='duty_step2_10013_ly']/li[1]/label")
elem.click()

elem = browser.find_element_by_xpath("//*[@id='devSearchForm']/div[2]/div/div[1]/dl[3]/dt/p") # 신입
elem.click()

elem = browser.find_element_by_xpath("//*[@id='devSearchForm']/div[2]/div/div[1]/dl[3]/dd/div[1]/ul[1]/li[1]/label")
elem.click()

elem = browser.find_element_by_xpath("//*[@id='devSearchForm']/div[2]/div/div[1]/dl[2]/dt/p") # 지역(서울/경기)
elem.click()

elem = browser.find_element_by_xpath("//*[@id='devSearchForm']/div[2]/div/div[1]/dl[2]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[1]/label")
elem.click()

elem = browser.find_element_by_xpath("//*[@id='devSearchForm']/div[2]/div/div[1]/dl[2]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[2]/label")
elem.click()

elem = browser.find_element_by_xpath("//*[@id='dev-btn-search']")
elem.click()

# 헤드라인, 추천, 핵심 채용관 정보 추가
time.sleep(interval) # 주요채용
soup = bs(browser.page_source, "lxml")
h_here = soup.find_all("li", attrs={"class": "itemBgTop devloopArea"})
for h in h_here:
    try:
        c = h.find("div", attrs={"class": "company"})
        t = h.find("div", attrs={"class": "description"})
        d = h.find("span", attrs={"class": "deadLine"})
        l = h.find("a", attrs={"class": "effectLog"})
        company = c.text.strip()
        title = t.text.strip()
        date = d.text.strip()
        link = "http://www.jobkorea.co.kr/"+l['href']
    except:
        pass
    write_ws.append([company, title, date, link])

time.sleep(interval)
soup = bs(browser.page_source, "lxml")
h_here = soup.find_all("li", attrs={"class": "itemBg devloopArea"})
for h in h_here:
    try:
        c = h.find("div", attrs={"class": "company"})
        t = h.find("div", attrs={"class": "description"})
        d = h.find("span", attrs={"class": "deadLine"})
        l = h.find("a", attrs={"class": "effectLog"})
        company = c.text.strip()
        title = t.text.strip()
        date = d.text.strip()
        link = "http://www.jobkorea.co.kr/"+l['href']
    except:
        pass
    write_ws.append([company, title, date, link])

time.sleep(interval)
h_here = soup.find_all("li", attrs={"class": " devloopArea"})
for h in h_here:
    try:
        c = h.find("div", attrs={"class": "company"})
        t = h.find("div", attrs={"class": "description"})
        d = h.find("span", attrs={"class": "deadLine"})
        l = h.find("a", attrs={"class": "effectLog"})
        company = c.text.strip()
        title = t.text.strip()
        date = d.text.strip()
        link = "http://www.jobkorea.co.kr/"+l['href']
    except:
        pass
    write_ws.append([company, title, date, link])
# 중복 데이터 제거

# 공고 검색 시작
for i in range(1, 11):
    soup = bs(browser.page_source, "lxml")
    m_here = soup.find_all("tr", attrs={"class": "devloopArea"})
    for m in m_here:
        try:
            c = m.find("a", attrs={"class": "link normalLog", "data-clickctgrcode":"B01"})
            t = m.find("a", attrs={"class": "link normalLog", "data-clickctgrcode":"B02"})
            d = m.find("span", attrs={"class": "date dotum"})
            company = c.text.strip()
            title = t.text.strip()
            date = d.text.strip()
            link = "http://www.jobkorea.co.kr/"+t['href']
        except:
            pass
        write_ws.append([company, title, date, link])
    
    write_wb.save("maketing_{}.xlsx".format(today))
    if i == 1:
        break

# df = pd.read_excel("maketing{}.xlsx".format(today))
# df.drop_duplicates(['회사명', '공고명'])


