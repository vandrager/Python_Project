# review data timegraph analysis
'''
[v] 월별 브랜드 별점 및 주문건수 추이 분석
[v] 평일/주말 그룹구분 or 브랜드별 주문건수 추이 분석(weekday)
[v] 브랜드별 주문건수 추이 시각화(Y)
[v] 브랜드별 월 주문건수 추이 분석(M)
'''

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib as mat
import seaborn as sns
mat.rcParams['font.family'] = 'Noto Sans CJK KR'


os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
df = pd.read_excel("sample.xlsx")

# 월별 브랜드 별점 및 주문건수 추이 분석
'''
df1 = df.groupby(df['월'])
brand = ['피자헛', '파파존스피자', '도미노피자', '반올림피자샵', '미스터피자', '피자마루', '피자알볼로', '피자나라치킨공주', '7번가피자', '김준현의피자헤븐']
for key, group in df1:
    print(f"* key :{key}월")
    print("* number :", len(group))
    for i in brand:
        mean = round(group[group['브랜드명'] ==i]['별점'].mean(), 2)
        count = group[group['브랜드명'] ==i]['별점'].count()
        if count == np.nan:
            count = 0
        print(f">> {i}: {mean}점({count})")
    print("")
'''
'''
* key :1월
* number : 2138
>> 피자헛: 4.47점(301)
>> 파파존스피자: 4.68점(175)
>> 도미노피자: 4.47점(137)
>> 반올림피자샵: 4.71점(536)
>> 미스터피자: 4.39점(149)
>> 피자마루: 4.58점(40)
>> 피자알볼로: 4.62점(159)
>> 피자나라치킨공주: 4.62점(253)
>> 7번가피자: 4.85점(280)
>> 김준현의피자헤븐: 4.73점(108)

* key :2월
* number : 1747
>> 피자헛: 4.54점(317)
>> 파파존스피자: 4.58점(153)
>> 도미노피자: 4.51점(92)
>> 반올림피자샵: 4.72점(404)
>> 미스터피자: 4.56점(127)
>> 피자마루: 4.62점(26)
>> 피자알볼로: 4.66점(188)
>> 피자나라치킨공주: 4.69점(169)
>> 7번가피자: 4.81점(218)
>> 김준현의피자헤븐: 4.62점(53)

* key :3월
* number : 2085
>> 피자헛: 4.58점(361)
>> 파파존스피자: 4.65점(146)
>> 도미노피자: 4.71점(89)
>> 반올림피자샵: 4.78점(481)
>> 미스터피자: 4.43점(339)
>> 피자마루: 4.77점(43)
>> 피자알볼로: 4.64점(168)
>> 피자나라치킨공주: 4.66점(173)
>> 7번가피자: 4.72점(231)
>> 김준현의피자헤븐: 4.65점(54)

* key :4월
* number : 1770
>> 피자헛: 4.58점(358)
>> 파파존스피자: 4.63점(158)
>> 도미노피자: 4.66점(90)
>> 반올림피자샵: 4.75점(405)
>> 미스터피자: 4.42점(139)
>> 피자마루: 4.56점(36)
>> 피자알볼로: 4.69점(143)
>> 피자나라치킨공주: 4.42점(188)
>> 7번가피자: 4.85점(208)
>> 김준현의피자헤븐: 4.51점(45)

* key :5월
* number : 1677
>> 피자헛: 4.64점(355)
>> 파파존스피자: 4.6점(136)
>> 도미노피자: 4.37점(73)
>> 반올림피자샵: 4.73점(421)
>> 미스터피자: 4.61점(103)
>> 피자마루: 4.92점(24)
>> 피자알볼로: 4.75점(130)
>> 피자나라치킨공주: 4.56점(185)
>> 7번가피자: 4.83점(195)
>> 김준현의피자헤븐: 4.84점(55)

* key :6월
* number : 2041
>> 피자헛: 4.56점(327)
>> 파파존스피자: 4.66점(244)
>> 도미노피자: 4.66점(87)
>> 반올림피자샵: 4.78점(425)
>> 미스터피자: 4.54점(128)
>> 피자마루: 4.82점(33)
>> 피자알볼로: 4.73점(299)
>> 피자나라치킨공주: 4.63점(219)
>> 7번가피자: 4.86점(214)
>> 김준현의피자헤븐: 4.65점(65)

* key :7월
* number : 2279
>> 피자헛: 4.61점(495)
>> 파파존스피자: 4.64점(181)
>> 도미노피자: 4.62점(64)
>> 반올림피자샵: 4.72점(520)
>> 미스터피자: 4.65점(120)
>> 피자마루: 4.77점(48)
>> 피자알볼로: 4.75점(224)
>> 피자나라치킨공주: 4.69점(278)
>> 7번가피자: 4.84점(259)
>> 김준현의피자헤븐: 4.47점(90)

* key :8월
* number : 2468
>> 피자헛: 4.61점(430)
>> 파파존스피자: 4.67점(201)
>> 도미노피자: 4.73점(126)
>> 반올림피자샵: 4.74점(544)
>> 미스터피자: 4.49점(180)
>> 피자마루: 4.57점(49)
>> 피자알볼로: 4.71점(247)
>> 피자나라치킨공주: 4.53점(273)
>> 7번가피자: 4.83점(324)
>> 김준현의피자헤븐: 4.68점(94)

* key :9월
* number : 2134
>> 피자헛: 4.68점(346)
>> 파파존스피자: 4.77점(149)
>> 도미노피자: 4.58점(128)
>> 반올림피자샵: 4.77점(495)
>> 미스터피자: 4.53점(132)
>> 피자마루: 4.63점(46)
>> 피자알볼로: 4.77점(244)
>> 피자나라치킨공주: 4.68점(246)
>> 7번가피자: 4.82점(274)
>> 김준현의피자헤븐: 4.61점(74)

* key :10월
* number : 2110
>> 피자헛: 4.58점(313)
>> 파파존스피자: 4.61점(135)
>> 도미노피자: 4.54점(89)
>> 반올림피자샵: 4.77점(558)
>> 미스터피자: 4.56점(151)
>> 피자마루: 4.59점(29)
>> 피자알볼로: 4.69점(161)
>> 피자나라치킨공주: 4.55점(239)
>> 7번가피자: 4.84점(322)
>> 김준현의피자헤븐: 4.45점(113)

* key :11월
* number : 2318
>> 피자헛: 4.54점(328)
>> 파파존스피자: 4.73점(139)
>> 도미노피자: 4.65점(109)
>> 반올림피자샵: 4.71점(523)
>> 미스터피자: 4.46점(151)
>> 피자마루: 4.71점(35)
>> 피자알볼로: 4.77점(311)
>> 피자나라치킨공주: 4.6점(264)
>> 7번가피자: 4.88점(361)
>> 김준현의피자헤븐: 4.66점(97)

* key :12월
* number : 2871
>> 피자헛: 4.57점(394)
>> 파파존스피자: 4.6점(190)
>> 도미노피자: 4.63점(102)
>> 반올림피자샵: 4.78점(784)
>> 미스터피자: 4.31점(221)
>> 피자마루: 4.52점(63)
>> 피자알볼로: 4.71점(281)
>> 피자나라치킨공주: 4.58점(331)
>> 7번가피자: 4.81점(377)
>> 김준현의피자헤븐: 4.64점(128)
'''

week_day = ['Monday', 'Tuesday', 'Wednesday', 'Friday', 'Thursday']
week_end = ['Saturday', 'Sunday']

# 평일/주말 그룹구분 or 브랜드별 주문건수 추이 분석(weekday)
df2 = df.groupby(df['브랜드명'])
'''
for key, group in df2:
    print(f"* Brand :{key}")
    print("* Total :", len(group))
    star_day = 0
    count_day = 0
    star_end = 0
    count_end = 0
    for k in week_day:
        star_day += group[group['weekday'] == k]['별점'].mean()
        count_day += group[group['weekday'] == k]['별점'].count()
    for j in week_end:
        star_end += group[group['weekday'] == j]['별점'].mean()
        count_end += group[group['weekday'] == j]['별점'].count()
    day_mean = round((star_day/5), 2)
    end_mean = round((star_end/2), 2)
    day_per = round((count_day/len(group))*100, 2)
    end_per = round((count_end/len(group))*100, 2)
    print(f">> 평일: {day_mean}점, ({count_day}개({day_per}%))")
    print(f">> 주말: {end_mean}점, ({count_end}개({end_per}%))")
    print("")
'''
'''
* Brand :7번가피자
* Total : 3263
>> 평일: 4.84점, (2288개(70.12%))
>> 주말: 4.8점, (975개(29.88%))

* Brand :김준현의피자헤븐
* Total : 976
>> 평일: 4.61점, (636개(65.16%))
>> 주말: 4.62점, (340개(34.84%))

* Brand :도미노피자
* Total : 1186
>> 평일: 4.57점, (746개(62.9%))
>> 주말: 4.64점, (440개(37.1%))

* Brand :미스터피자
* Total : 1940
>> 평일: 4.49점, (1154개(59.48%))
>> 주말: 4.46점, (786개(40.52%))

* Brand :반올림피자샵
* Total : 6096
>> 평일: 4.76점, (3905개(64.06%))
>> 주말: 4.74점, (2191개(35.94%))

* Brand :파파존스피자
* Total : 2007
>> 평일: 4.64점, (1161개(57.85%))
>> 주말: 4.67점, (846개(42.15%))

* Brand :피자나라치킨공주
* Total : 2818
>> 평일: 4.63점, (1760개(62.46%))
>> 주말: 4.56점, (1058개(37.54%))

* Brand :피자마루
* Total : 472
>> 평일: 4.65점, (292개(61.86%))
>> 주말: 4.68점, (180개(38.14%))

* Brand :피자알볼로
* Total : 2555
>> 평일: 4.71점, (1652개(64.66%))
>> 주말: 4.73점, (903개(35.34%))

* Brand :피자헛
* Total : 4325
>> 평일: 4.59점, (2716개(62.8%))
>> 주말: 4.57점, (1609개(37.2%))
'''

# 브랜드별 주문건수 추이 시각화(Date)

# heatmap 그래프 출력하기(별점 평균/주문 건수)
df_pivot = df.pivot_table(index = '브랜드명', columns = '연', values = '별점', aggfunc = 'mean') # 브랜드별 연간 별점 평균
df2_pivot = df.pivot_table(index = '브랜드명', columns = '연', values = '별점', aggfunc = 'count') # 브랜드별 연간 주문건수
fig = plt.figure(figsize = (20, 10))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
sns.heatmap(df_pivot, cmap='Blues', annot = True, ax = ax1)
sns.heatmap(df2_pivot, cmap='YlGnBu', vmin=0, vmax=2500, ax = ax2)
plt.show()

# 주문건수 전체 비율 파이 그래프 만들기
fig = plt.figure(figsize=(20, 20))
plt.title("전체 주문건수 브랜드별 비율", size = 15)
plt.rcParams['font.size'] = 8

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
df2_pivot[2020].plot(kind = 'pie', autopct="%1.1f%%", startangle=10,
                        cmap= 'plasma', ax = ax1)
df2_pivot[2019].plot(kind = 'pie', autopct="%1.1f%%", startangle=10,
                        cmap= 'plasma', ax = ax2)
df2_pivot[2018].plot(kind = 'pie', autopct="%1.1f%%", startangle=10,
                        cmap= 'plasma', ax = ax3)
df2_pivot[2017].plot(kind = 'pie', autopct="%1.1f%%", startangle=10,
                        cmap= 'plasma', ax = ax4)
plt.show()

# 브랜드별 월간 별점/주문건수 그래프 만들기
df_pivot = df.pivot_table(index = '브랜드명', columns = '월', values = '별점', aggfunc = 'mean') # 브랜드별 월간 별점 평균
df2_pivot = df.pivot_table(index = '브랜드명', columns = '월', values = '별점', aggfunc = 'count') # 브랜드별 월간 주문건수
df2_pivot.plot(kind = 'line', cmap= 'plasma')
plt.show()
