# review data target analysis

'''
브랜드별 별점 평균 순위 확인
주문그룹별 주문건수 파악 및 주문그룹별 선호 메뉴구분 분석
브랜드 메뉴구분별 리뷰 키워드 top10 분석(기타 제외)
브랜드 메뉴구분별 별점 분포(boxplot) 분석
브랜드 대표메뉴(메뉴구분) 분석(값은 별점 합계로 계산)
별점 만족도별 메뉴구분 분석(1~2점 불만족, 3점 보통, 4~5점 만족)
서울권/비서울권 브랜드 별점 합계 & 리뷰 건수 파악을 통한 브랜드 선호도 파악
'''

import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup as bs
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook #  결과물을 엑셀 파일로 저장

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
'''
# 전체 데이터 불러온 뒤 샘플데이터 생성
df = pd.read_excel("review_final.xlsx")
sp = df.sample(frac = 0.1, replace = True)
sp.to_excel("sample.xlsx")
'''

df = pd.read_excel("sample.xlsx")
'''
# 주문그룹 구분 데이터 개수 확인
df1 = df.groupby(df['그룹구분'])

for key, group in df1:
    print("* key :", key)
    print("* number :", len(group))
    print('\n')

# 그룹별 주문건수
* key : Party
* number : 9189

* key : Side
* number : 6879

* key : Single
* number : 9570
'''

menu = ['베이컨', '고르곤졸라', '콤비네이션', '스테이크', '쉬림프', '포테이토', '치킨', '고구마', '불고기', '하와이안', '페페로니'] # 없으면 기타로 구분한다.

'''
# 메뉴구분 데이터 개수 확인
df2 = df.groupby(df['메뉴구분']) #메뉴구분

for i in menu:
    count = 0
    for key, group in df2:
        if i in key:
            count += len(group)
    print(f"* {i}: {count}")

* 베이컨: 780
* 고르곤졸라: 78
* 콤비네이션: 1973
* 스테이크: 1789
* 쉬림프: 1810
* 포테이토: 2595
* 치킨: 2017
* 고구마: 1068
* 불고기: 1239
* 하와이안: 257
* 페페로니: 543
'''


# 브랜드명 데이터 개수 확인 및 별점 평균 순위 확인
df3 = df.groupby(df['브랜드명'])
brand_list = []
mean_list = []
for key, group in df3:
    print("* key :", key)
    print("* number :", len(group))
    mean = round(group['별점'].mean(), 2)
    print(mean)
    mean_list.append(mean)
    brand_list.append(key)

rank = pd.Series(mean_list, index=brand_list)
print(rank.sort_values(ascending=False))
'''
* key : 7번가피자
* number : 3263
4.83
* key : 김준현의피자헤븐
* number : 976
4.62
* key : 도미노피자
* number : 1186
4.6
* key : 미스터피자
* number : 1940
4.48
* key : 반올림피자샵
* number : 6096
4.75
* key : 파파존스피자
* number : 2007
4.65
* key : 피자나라치킨공주
* number : 2818
4.6
* key : 피자마루
* number : 472
4.66
* key : 피자알볼로
* number : 2555
4.71
* key : 피자헛
* number : 4325
4.58

7번가피자       4.83
반올림피자샵      4.75
피자알볼로       4.71
피자마루        4.66
파파존스피자      4.65
김준현의피자헤븐    4.62
피자나라치킨공주    4.60
도미노피자       4.60
피자헛         4.58
미스터피자       4.48
'''

