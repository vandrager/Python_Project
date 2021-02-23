import os
import re
import pandas as pd
import numpy as np
from openpyxl import Workbook #  결과물을 엑셀 파일로 저장
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\2차 분석")
# df = pd.read_excel("sample.xlsx") # 샘플 데이터
write_wb = Workbook()
write_ws = write_wb.active
write_ws.append(["브랜드", "주문건수", "별점", "종합점수"])
df = pd.read_excel("Review.xlsx")
gdf = df.groupby(['브랜드명'])
for key, group in gdf:
    print("* key :", key)
    print("* number :", format(len(group['별점']), ","))
    size = len(group['별점'])
    mean = round(group['별점'].mean(), 3)
    print(mean)
    point = size*mean
    print(format(point, ","))
    write_ws.append([key, size, mean, point])
    print("")
write_wb.save("rank.xlsx")
'''
* key : 7번가피자
* number : 28,109
4.846
136,216.214

* key : 김준현의피자헤븐
* number : 8,742
4.681
40,921.302      

* key : 도미노피자
* number : 10,211 
4.641
47,389.251

* key : 미스터피자
* number : 12,885
4.539
58,485.015

* key : 반올림피자샵
* number : 39,949
4.775
190,756.475

* key : 파파존스피자
* number : 18,893
4.622
87,323.446

* key : 피자나라치킨공주
* number : 25,537
4.592
117,265.904

* key : 피자마루
* number : 3,802
4.661
17,721.122

* key : 피자알볼로
* number : 24,225
4.725
114,463.12499999999

* key : 피자헛
* number : 25,511
4.571
116,610.78099999999
'''
# gdf = df.groupby(['브랜드명', '메뉴구분'])['별점'].count()
# gdf.to_excel("test.xlsx")
# for key, group in gdf:
#     print("* key :", key)
#     print("* number :", format(len(group), ","))
#     mean = round(group['별점'].mean(), 2)
#     print(mean)

# 도우구분은 상관없이 그냥 가는걸로
# 14~16 분석, datastudio 분석
# django 웹 분석 프로그래밍 공부

'''
2021-02-19 ~ 2021-02-20
"PIDUK"(피자 덕후)
dashboard(Only 1page)
피자 마니아들을 위한 메뉴 추천 서비스
(필터) 1. 브랜드명 | 2. date(2016 ~ )
별점이 KPI니까 별점 평균값 구하고 /5 해서 퍼센티지 구하기
[스코어카드]
별점, 주문건수

[주문추이]
맛, 양, 배달 점수 삼각형 파이 그래프 -> 그룹구분별 영역 데이터 그래프 그리기
연도/월 그룹화 - 주말/평일 막대 그래프
브랜드 -> 메뉴 -> 그룹 퍼널 차트

[메뉴 추천]
best menu top5 - 이미지, 메뉴구분(그룹구분), 가격, 메뉴의 별점 합계/평균 점수

[그룹 그분 파이 그래프]

-가격대별 주문 추이
-그룹구분별 주문 추이
'''

'''
주말 여부 추가
CASE 
    WHEN weekday IN ("Thursday", "Tuesday", "Monday", "Wednesday",	"Friday") THEN "평일" 
    WHEN weekday IN ("Sunday",	"Saturday")THEN "주말" 
    ELSE "Other" 
END

CASE 
    WHEN 평균 점수 > 14.4 THEN "이 메뉴의 추천 정도는 '매우 높음' 입니다."
    WHEN 평균 점수 > 14.4 THEN "이 메뉴의 추천 정도는 '높음' 입니다."
    WHEN 평균 점수 > 14.4 THEN "이 메뉴의 추천 정도는 '보통' 입니다."
    ELSE "이 메뉴의 추천 정도는 '낮음' 입니다." 
END
---> 평균점수가 숫자이기에 THEN 이후 출력되어 나오는 형태도 숫자이어야함
'''