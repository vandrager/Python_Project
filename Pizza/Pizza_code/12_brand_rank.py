import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")

# 전체 데이터셋 불러오기
df = pd.read_excel("seoul_review.xlsx")

df['브랜드명'][df['브랜드명'] == "김준현의 피자헤븐"] = "김준현의피자헤븐"
# # 테스트 데이터셋 불러오기
# # df = pd.read_excel("test_data.xlsx")


# # 1. 브랜드별 별점, 맛, 양, 배달 평균값 및 count
brand_group = df.groupby(['브랜드명'])
print(round(brand_group['별점', '맛', '양', '배달'].mean(), 2), brand_group['리뷰'].count())
# '''
#                  별점     맛     양    배달
# 브랜드명
# 7번가피자          4.82  4.64  4.64  4.64
# 김준현의 피자헤븐      4.68  3.79  3.80  3.84
# 김준현의피자헤븐       4.66  4.27  4.31  4.30
# 도미노피자          4.64  4.60  4.61  4.74
# 미스터피자          4.52  4.46  4.52  4.53
# 미스터피자Single메뉴  4.51  4.48  4.42  4.52
# 반올림피자샵         4.73  4.46  4.48  4.42
# 파파존스피자         4.61  4.51  4.35  4.53
# 피자나라치킨공주       4.58  4.42  4.55  4.40
# 피자마루           4.64  4.61  4.62  4.61
# 피자알볼로          4.72  4.57  4.59  4.57
# 피자헛            4.59  4.46  4.47  4.59
#                     브랜드명
# 7번가피자            20276
# 김준현의 피자헤븐          874
# 김준현의피자헤븐          7599
# 도미노피자             5542
# 미스터피자            10538
# 미스터피자Single메뉴      434
# 반올림피자샵           35372
# 파파존스피자           13958
# 피자나라치킨공주         21283
# 피자마루              3548
# 피자알볼로            14169
# 피자헛              24638
# Name: 리뷰, dtype: int64
# '''

# # 2. 평일/주말 및 요일별 고객 주문 건수 분석
# # 평일 주말 고객 주문 건수 비교
# weekday = 'Thursday	Tuesday	Monday	Wednesday	Friday'.split("\t")
# weekend = 'Sunday	Saturday'.split("\t")
# daycount = 0 # 평일 주문량 합계
# endcount = 0 # 주말 주문량 합계
# for i in df['weekday']:
#     if i in weekday:
#         daycount += 1
#     elif i in weekend:
#         endcount += 1

# print(daycount, endcount) # 평일 주문 건수 & 주말 주문 건수
# print(round(daycount/len(df), 3), round(endcount/len(df), 3))  # 평일 주문 비율 & 주말 주문 비율

# # 요일별 고객 주문 건수
# print(df.groupby(['weekday'])['시'].count())
# '''
# 99440 58791
# 0.628 0.372
# weekday
# Friday       21216
# Monday       20216
# Saturday     27036
# Sunday       31755
# Thursday     20639
# Tuesday      19014
# Wednesday    18355
# Name: 시, dtype: int64
# '''
