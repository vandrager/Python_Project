import os, re, usecsv
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook #  결과물을 엑셀 파일로 저장
 

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
file = pd.read_csv("seoul_random.csv", encoding = "cp949")
brand = ['피자헛', '파파존스', '도미노피자', '반올림피자샵', '미스터피자', '피자마루', '피자알볼로', '피자나라치킨공주', '7번가피자', '피자헤븐']

interval = 3 # 3초에 한번씩 스크롤 내림(많아서 렉걸릴 수 있으니 좀 길게 설정)
browser = webdriver.Chrome("C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Python/webscraping_basic/chromedriver.exe")
browser.maximize_window()
time.sleep(interval)


# 지역구별 피자집 검색 시작
# 23일 15시 기준 성북구까지 했고 동대문구 에러 발생, 17부터 시작
# 동대문구 10 김준현의 피자헤븐 회기점 검색 x 문제 이후 수정
# 목동 18번 피자마루-목동2호점 리뷰 5개 짜리라 문제 발생 이후 수정
# 은평구 21번도 위와 동일문제 발생
# 마지막 중랑구 24번 시간 문제로 중단, 기본 코드로 다시 디버그해볼것
# 추후 금천구(7) 데이터셋 길이 확인
for i in range(24, 25):
    write_wb = Workbook()
    write_ws = write_wb.active
    browser.get("https://www.yogiyo.co.kr/mobile/#/")
    elem = browser.find_element_by_name("address_input")
    elem.click()
    elem.clear()

    # 해당 지역구 주소 입력

    elem.send_keys(file['주소'][i]) # 브랜드 이름도 자동화
    elem.send_keys(Keys.ENTER)
    time.sleep(interval)

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

    # match리스트 안에 들어있는 피자집
    for j in range(len(match)):
        elem = browser.find_element_by_css_selector("#category > ul > li.hidden-xs.menu-search > a")
        time.sleep(2)
        elem.click()
        time.sleep(2)

        elem = browser.find_element_by_xpath("//*[@id='category']/ul/li[15]/form/div/input")
        elem.send_keys(match[j])
        elem.send_keys(Keys.ENTER)
        time.sleep(interval)
        
        elem = browser.find_element_by_css_selector("#content > div > div:nth-child(5) > div > div > div > div")
        elem.click()
        time.sleep(interval)


        
        elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/ul/li[2]/a")
        elem.click()
        time.sleep(2)

        elem = browser.find_element_by_xpath("//*[@id='review']/li[12]")

        # 해당 피자 브랜드 리뷰 전체 스크롤 시작
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        prev_height = browser.execute_script("return document.body.scrollHeight")


        while True:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            try:
                elem.click()
            except:
                pass
            
            # 페이지 로딩 대기
            time.sleep(interval)


            # 현재 문서 높이를 가져와서 저장
            curr_height = browser.execute_script("return document.body.scrollHeight")
            if curr_height == prev_height:
                break

            prev_height = curr_height

        print("리뷰 스크롤 완료")
        # 피자 브랜드 리뷰 스크래핑
        soup = bs(browser.page_source, "lxml")
        # page_source로 스크롤 끝까지 내렸을 때의 html 정보를 가져오게 됨

        # reviews = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
        reviews = soup.find_all("li", attrs={"class": "list-group-item star-point ng-scope"})
        print(len(reviews))


        for review in reviews:
            taste = review.find("span", attrs={"class": "points ng-binding", "ng-show":"review.rating_taste > 0"})
            quantity = review.find("span", attrs={"class": "points ng-binding", "ng-show":"review.rating_quantity > 0"})
            delivery = review.find("span", attrs={"class": "points ng-binding", "ng-show":"review.rating_delivery > 0"})
            eat_menu = review.find("div", attrs={"class": "order-items default ng-binding", "ng-click": "show_review_menu($event)"})
            com_menu = review.find("p", attrs={"class": "ng-binding", "ng-show": "review.comment"})
            day = review.find("span", attrs = {"ng-bind": "review.time|since", "class": "review-time ng-binding"})
            star = review.find_all("span", attrs = {"class": "full ng-scope"})
            # <span class="points ng-binding" ng-show="review.rating_taste &gt; 0">5</span> 여기서 5만 가져오려면 get_text() or text
            # try! 이전 자료는 별점이 없기 때문에 리뷰와 주문 메뉴밖에 확인하지 못한다.
            try:
                star_point = int(len(star))
                taste_point = int(taste.text)
                quantity_point = int(quantity.text)
                delivery_point = int(delivery.text)
                menu = eat_menu.text.strip()
                comment = com_menu.text.strip()
                date = day.text.strip()
            except:
                star_point = int(len(star))
                taste_point = 0
                quantity_point = 0
                delivery_point = 0
                menu = eat_menu.text.strip()
                comment = com_menu.text.strip()
                date = day.text.strip()
            write_ws.append([file['주소'][i], match[j], date, menu, star_point, taste_point, quantity_point, delivery_point, comment])
        browser.back()
    write_wb.save("seoul_{}.xlsx".format(i+1))