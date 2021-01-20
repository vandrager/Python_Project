import os, re, usecsv
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Python/webscraping_basic/chromedriver.exe")
browser.get("https://www.yogiyo.co.kr/mobile/#/452598/")
browser.maximize_window()
elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/ul/li[2]/a")
elem.click()

elem = browser.find_element_by_xpath("//*[@id='review']/li[12]")

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
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

print("스크롤 완료")




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

for review in reviews:
    taste = review.find("span", attrs={"class": "points ng-binding", "ng-show":"review.rating_taste > 0"})
    quantity = review.find("span", attrs={"class": "points ng-binding", "ng-show":"review.rating_quantity > 0"})
    delivery = review.find("span", attrs={"class": "points ng-binding", "ng-show":"review.rating_delivery > 0"})
    # <span class="points ng-binding" ng-show="review.rating_taste &gt; 0">5</span> 여기서 5만 가져오려면 get_text() or text
    review_point = (int(taste.text) + int(quantity.text) + int(delivery.text))/3
    taste_point = int(taste.text)
    quantity_point = int(quantity.text)
    delivery_point = int(delivery.text)
    total_average += review_point
    taste_average += taste_point
    quantity_average += quantity_point
    delivery_average += delivery_point



print("-" * 25 + "[    Result    ]" + "-" * 25)
print(f"전체 평점 : {round(total_average/len(reviews), 1)}")
print(f"맛 평점 : {round(taste_average/len(reviews), 1)}")
print(f"양 평점 : {round(quantity_average/len(reviews), 1)}")
print(f"배달 평점 : {round(delivery_average/len(reviews), 1)}")

'''
---------------------------[    Result    ]-----------------------------
전체 평점 : 4.8
맛 평점 : 4.8
양 평점 : 4.8
배달 평점 : 4.8
'''