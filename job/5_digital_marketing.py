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

# 공고 선택 조건 세팅(마케팅/신입)
elem = browser.find_element_by_xpath("//*[@id='devSearchForm']/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[2]/label")
elem.click()

elem = browser.find_element_by_xpath("//*[@id='duty_step2_10013_ly']/li[1]/label")
elem.click()

elem = browser.find_element_by_xpath("//*[@id='devSearchForm']/div[2]/div/div[1]/dl[3]/dt/p")
elem.click()

elem = browser.find_element_by_xpath("//*[@id='devSearchForm']/div[2]/div/div[1]/dl[3]/dd/div[1]/ul[1]/li[1]/label")
elem.click()

elem = browser.find_element_by_xpath("//*[@id='dev-btn-search']")
elem.click()

# 공고 검색 시작
for i in range(1, 11):
    print("공고 리스트 스크롤 완료")
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
            link = t['href']
        except:
            pass
        write_ws.append([company, title, date, link])
    write_wb.save("maketing{}.xlsx".format(today))
    if i == 1:
        break


