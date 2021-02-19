import os
import re
import pandas as pd
import numpy as np

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\2차 분석")
# df = pd.read_excel("sample.xlsx") # 샘플 데이터

df = pd.read_excel("Review.xlsx")

gdf = df.groupby(['브랜드명', '메뉴구분'])['별점'].count()
gdf.to_excel("test.xlsx")
# for key, group in gdf:
#     print("* key :", key)
#     print("* number :", format(len(group), ","))
#     mean = round(group['별점'].mean(), 2)
#     print(mean)

# 도우구분은 상관없이 그냥 가는걸로
# 14~16 분석, datastudio 분석
# django 웹 분석 프로그래밍 공부

'''
2021-02-19
dashboard(1page)
피자 마니아들을 위한 메뉴 추천 서비스
(필터) 1. 브랜드명 | 2. date(2016 ~ )

[스코어카드]
별점, 주문건수

[주문추이]
맛, 양, 배달 점수 삼각형 파이 그래프
연도/월 그룹화 - 주말/평일 막대 그래프
브랜드 -> 메뉴 -> 그룹 퍼널 차트

[메뉴 추천]
best menu top5 - 이미지, 메뉴구분(그룹구분), 가격, 메뉴의 별점 합계/평균 점수

[그룹 그분 파이 그래프]
'''
