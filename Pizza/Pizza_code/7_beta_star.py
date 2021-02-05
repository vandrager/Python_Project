import os, re, usecsv
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from collections import Counter # Counter: 리스트에서 모든 아이템을 count 하고 싶을 때 사용
# result = Counter(myList)
# for key in result:
#     print key, result[key]
from openpyxl import Workbook #  결과물을 엑셀 파일로 저장



os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")



write_wb = Workbook()
write_ws = write_wb.active
interval = 2
browser = webdriver.Chrome("C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Python/webscraping_basic/chromedriver.exe")
browser.maximize_window()
browser.get("https://www.yogiyo.co.kr/mobile/#/229976/")
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

# 정보) 속성을 리스트로 감싸주어 조건을 만족하는 모든 데이터를 가져올 수 있다.
# reviews = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
reviews = soup.find_all("li", attrs={"class": "list-group-item star-point ng-scope"})
print(len(reviews))
total_average = 0 # 리뷰 전체 평균
taste_average = 0 # 맛 전체 평균
quantity_average = 0 # 양 전체 평균
delivery_average = 0 # 배달 전체 평균
menu = []
comment = []


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
    '''
    ### 움... 리뷰 정보가 제대로 안나오고 중복되어 나타나는 현상이 발생!! 어떡할까요..?
    리뷰 뿐만 아니라 맛, 양, 배달 점수 정보도 중복되어 출력됨
    엑셀 자치구별로 한개씩 저장하는 것은 지금 매우 잘되는 중임!
    총 별점 5개도 정보로 기록하면 좋을 듯
    한 엑셀 파일에 워크시트만 따로하는 방법은 무엇??
    날짜 만들어 놓고 왜 추가는 안했니... ㅠ
    '''
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
    write_ws.append([date, menu, star_point, taste_point, quantity_point, delivery_point, comment])
write_wb.save("gangnam_papa.xlsx")

