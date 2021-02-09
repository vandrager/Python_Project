import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mat
mat.rcParams['font.family'] = 'Noto Sans CJK KR'
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")

# 전체 데이터셋 불러오기
df = pd.read_excel("sample.xlsx")

# 테스트 데이터셋 불러오기
# df = pd.read_excel("test_data.xlsx")


# # 1. 브랜드별 별점, 맛, 양, 배달 평균값 및 count
brand_group = df.groupby(['브랜드명'])
print(round(brand_group['별점', '맛', '양', '배달'].mean(), 2), brand_group['리뷰'].count())
'''
            별점     맛     양    배달  
브랜드명                                
7번가피자     4.83  4.71  4.70  4.71    
김준현의피자헤븐  4.62  4.31  4.34  4.31
도미노피자     4.60  4.58  4.56  4.69   
미스터피자     4.48  4.42  4.51  4.48   
반올림피자샵    4.75  4.53  4.56  4.50  
파파존스피자    4.65  4.57  4.43  4.58  
피자나라치킨공주  4.60  4.45  4.58  4.42
피자마루      4.66  4.58  4.61  4.61
피자알볼로     4.71  4.55  4.57  4.55
피자헛       4.58  4.46  4.48  4.57

브랜드명
7번가피자       3263
김준현의피자헤븐     976
도미노피자       1186
미스터피자       1940
반올림피자샵      6096
파파존스피자      2007
피자나라치킨공주    2818
피자마루         472
피자알볼로       2555
피자헛         4325
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
평일 >  16310 주말 >  9328
63.6% (평일) 36.4% (주말)
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

2015       50
2016      313
2017     1222
2018     3914
2019     8931
2020    10628
2021      580
Name: 리뷰, dtype: int64

월
1     2138
2     1747
3     2085
4     1770
5     1677
6     2041
7     2279
8     2468
9     2134
10    2110
11    2318
12    2871
Name: 리뷰, dtype: int64

weekday
Friday       3559
Monday       3284
Saturday     4209
Sunday       5119
Thursday     3442
Tuesday      3011
Wednesday    3014
Name: 리뷰, dtype: int64
'''
# 브랜드 월 평균 별점 분석
pdf = pd.pivot_table(df,
                        index="브랜드명",
                        columns="월",
                        values="별점",
                        aggfunc='mean')
print(round(pdf, 2))
'''
월           1     2     3     4     5     6     7     8     9     10    11    12
브랜드명
7번가피자     4.85  4.81  4.72  4.85  4.83  4.86  4.84  4.83  4.82  4.84  4.88  4.81
김준현의피자헤븐  4.73  4.62  4.65  4.51  4.84  4.65  4.47  4.68  4.61  4.45  4.66  4.64
도미노피자     4.47  4.51  4.71  4.66  4.37  4.66  4.62  4.73  4.58  4.54  4.65  4.63
미스터피자     4.39  4.56  4.43  4.42  4.61  4.54  4.65  4.49  4.53  4.56  4.46  4.31
반올림피자샵    4.71  4.72  4.78  4.75  4.73  4.78  4.72  4.74  4.77  4.77  4.71  4.78
파파존스피자    4.68  4.58  4.65  4.63  4.60  4.66  4.64  4.67  4.77  4.61  4.73  4.60
피자나라치킨공주  4.62  4.69  4.66  4.42  4.56  4.63  4.69  4.53  4.68  4.55  4.60  4.58
피자마루      4.58  4.62  4.77  4.56  4.92  4.82  4.77  4.57  4.63  4.59  4.71  4.52
피자알볼로     4.62  4.66  4.64  4.69  4.75  4.73  4.75  4.71  4.77  4.69  4.77  4.71
피자헛       4.47  4.54  4.58  4.58  4.64  4.56  4.61  4.61  4.68  4.58  4.54  4.57
'''
plt.figure(figsize = (20, 10))
sns.heatmap(pdf, cmap='Blues', annot = True)
plt.show()