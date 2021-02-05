import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")

# 전체 데이터셋 불러오기
df = pd.read_excel("seoul_review.xlsx")

# 테스트 데이터셋 불러오기
# df = pd.read_excel("test_data.xlsx")


# # 1. 브랜드별 별점, 맛, 양, 배달 평균값 및 count
brand_group = df.groupby(['브랜드명'])
print(round(brand_group['별점', '맛', '양', '배달'].mean(), 2), brand_group['리뷰'].count())
'''
            별점     맛     양    배달
브랜드명
7번가피자     4.82  4.64  4.64  4.64
김준현의피자헤븐  4.66  4.22  4.25  4.25
도미노피자     4.64  4.60  4.61  4.74
미스터피자     4.52  4.46  4.51  4.53
반올림피자샵    4.73  4.46  4.48  4.42
파파존스피자    4.61  4.51  4.35  4.53
피자나라치킨공주  4.58  4.42  4.55  4.40
피자마루      4.64  4.61  4.62  4.61
피자알볼로     4.72  4.57  4.59  4.57
피자헛       4.59  4.46  4.47  4.59

            브랜드명
7번가피자       20276
김준현의피자헤븐     8473
도미노피자        5542
미스터피자       10972
반올림피자샵      35372
파파존스피자      13958
피자나라치킨공주    21283
피자마루         3548
피자알볼로       14169
피자헛         24638
Name: 리뷰, dtype: int64
'''

# 2. 평일/주말 및 요일별 고객 주문 건수 분석
# 평일 주말 고객 주문 건수 비교
weekday = 'Thursday	Tuesday	Monday	Wednesday	Friday'.split("\t")
weekend = 'Sunday	Saturday'.split("\t")
daycount = 0 # 평일 주문량 합계
endcount = 0 # 주말 주문량 합계
for i in df['weekday']:
    if i in weekday:
        daycount += 1
    elif i in weekend:
        endcount += 1

print("평일 > ", daycount, "주말 > ",endcount) # 평일 주문 건수 & 주말 주문 건수
print(f"{round(daycount/len(df), 3)*100}% (평일)", f"{round(endcount/len(df), 3)*100}% (주말)")  # 평일 주문 비율 & 주말 주문 비율
print("")
'''
평일 >  99440 주말 >  58791
62.8% (평일) 37.2% (주말)
'''
# 연도별 고객 주문 건수
print(df.groupby(['연'])['리뷰'].count())
print("")

# 월별 고객 주문 건수
print(df.groupby(['월'])['리뷰'].count())
print("")

# 요일별 고객 주문 건수
print(df.groupby(['weekday'])['리뷰'].count())
print("")
'''
연
2015      325
2016     2422
2017     8778
2018    27242
2019    55281
2020    61437
2021     2746
Name: 리뷰, dtype: int64

월
1     12544
2     10364
3     12614
4     11037
5     10785
6     13038
7     14505
8     14809
9     12991
10    13409
11    14367
12    17768
Name: 리뷰, dtype: int64

weekday
Friday       21216
Monday       20216
Saturday     27036
Sunday       31755
Thursday     20639
Tuesday      19014
Wednesday    18355
Name: 시, dtype: int64
'''
# 브랜드 월 평균 별점 분석
pdf = pd.pivot_table(df,
                        index="브랜드명",
                        columns="월",
                        values="별점",
                        aggfunc='mean')
print(round(pdf, 1))
'''
월          1    2    3    4    5    6    7    8    9    10   11   12
브랜드명
7번가피자     4.8  4.8  4.8  4.8  4.8  4.8  4.8  4.8  4.8  4.9  4.9  4.8
김준현의피자헤븐  4.7  4.6  4.6  4.7  4.7  4.7  4.7  4.7  4.6  4.7  4.6  4.7
도미노피자     4.6  4.7  4.7  4.7  4.5  4.7  4.6  4.7  4.6  4.7  4.7  4.6
미스터피자     4.5  4.4  4.5  4.6  4.6  4.6  4.6  4.6  4.5  4.6  4.5  4.5
반올림피자샵    4.7  4.7  4.7  4.7  4.7  4.7  4.7  4.8  4.7  4.7  4.7  4.7
파파존스피자    4.6  4.5  4.6  4.6  4.7  4.6  4.6  4.7  4.7  4.7  4.6  4.6
피자나라치킨공주  4.6  4.5  4.6  4.6  4.6  4.6  4.5  4.5  4.6  4.6  4.6  4.6
피자마루      4.7  4.6  4.7  4.6  4.6  4.6  4.7  4.7  4.6  4.6  4.6  4.7
피자알볼로     4.7  4.7  4.7  4.7  4.7  4.7  4.7  4.7  4.7  4.7  4.8  4.7
피자헛       4.5  4.6  4.6  4.6  4.6  4.6  4.6  4.6  4.6  4.6  4.6  4.5
'''
