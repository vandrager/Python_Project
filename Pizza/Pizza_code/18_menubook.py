import os
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook #  결과물을 엑셀 파일로 저장


os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\hoho")
brand = ['피자헛', '파파존스', '도미노피자', '반올림피자샵', '미스터피자', '피자마루', '피자알볼로', '피자나라치킨공주', '7번가피자', '피자헤븐']

interval = 3 # 3초에 한번씩 스크롤 내림
browser = webdriver.Chrome("C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Python/webscraping_basic/chromedriver.exe")
browser.maximize_window()

# 지역구별 피자집 검색 시작
for i in range(9):
    write_wb = Workbook()
    write_ws = write_wb.active
    browser.get("https://www.yogiyo.co.kr/mobile/#/")
    elem = browser.find_element_by_name("address_input")

    elem.click()
    elem.clear()

    # 해당 지역구 주소 입력

    elem.send_keys("서울특별시 서대문구 남가좌동 증가로 150") # 브랜드 이름도 자동화
    elem.send_keys(Keys.ENTER)
    time.sleep(2)

    # 해당 지역구 피자 브랜드 검색

    elem = browser.find_element_by_xpath("//*[@id='category']/ul/li[6]")
    elem.click()

    # 화면 가장 아래로 스크롤 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 현재 문서 높이를 가져와서 저장
    prev_height = browser.execute_script("return document.body.scrollHeight")

    # 반복 수행
    while True:
        # 스크롤을 가장 아래로 내림
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        
        # 페이지 로딩 대기
        time.sleep(interval)


        # 현재 문서 높이를 가져와서 저장
        curr_height = browser.execute_script("return document.body.scrollHeight")
        if curr_height == prev_height:
            break

        prev_height = curr_height
    
    # 해당 지역구 피자 브랜드 리스트 스크롤

    print("브랜드 리스트 스크롤 완료")

    brand_list = []
    soup = bs(browser.page_source, "lxml")
    brand_here = soup.find_all("div", attrs={"class": "restaurant-name ng-binding"})
    for k in brand_here:
        brand_list.append(k['title'])

    # 파이썬: 리스트 안에 특정 문자열을 포함했는지 알아보기
    match_list = []
    for p in brand:
        for k in brand_list:
            if p in k:
                match_list.append(k)

    # 지역구 내 TOP10 피자집 리스트 검색 후 match 리스트에 저장
    match = list(set(match_list))
    print(match)

# 12일 이후 브랜드와 메뉴 스크롤하기

        print("메뉴 스크롤 완료")
        # 피자 브랜드별 메뉴 스크래핑
        soup = bs(browser.page_source, "lxml")
        items = soup.find_all("li", attrs={"ng-class": "get_menu_item_class(item)"})

        for pizza in items:
            name = pizza.find("div", attrs={"class": "menu-name ng-binding", "ng-bind-html":"item.name|strip_html"})
            image = pizza.find("div", attrs={"class": "photo"})

            try:
                price = pizza.find("span", attrs={"class": "ng-binding", "ng-bind": "item.price|krw"})
                p = price.text.strip()
                n = name.text.strip()
                i = image['style']
            except:
                price = pizza.find("span", attrs={"ng-show": "is_discount(item)", "ng-bind": "get_discounted_price(item)|krw"})
                p = price.text()
                n = name.text()
                i = image['style']
            write_ws.append([match[j], p, n, i])
        browser.back()
    write_wb.save("menubook{}.xlsx".format(i+1))