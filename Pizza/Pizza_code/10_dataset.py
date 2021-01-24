# 서울 전 지역 데이터 통합
# 1. 추출한 엑셀파일을 불러와 concat으로 합친다.
# 2. 지점 중복이 있을 수 있으므로 지점을 기준으로 중복값을 제거한다.
# df.drop_duplicates(subset=['지점'], inplace = True)
# 3. 중복을 제외한 자치구, 지점명만 가져와 하나의 데이터 프레임으로 만들어준다.
# line = df.loc[:,  ["자치구", "지점"]]
from collections import Counter # Counter: 리스트에서 모든 아이템을 count 하고 싶을 때 사용

import pandas as pd
import os
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")

'''
자치구별 피자 리뷰 데이터에 컬럼 넣어주기
for i in range(1, 26):
    file = pd.read_excel("seoul_{}.xlsx".format(i))
    file.columns = "자치구	브랜드	일자	주문메뉴	별점	맛	양	배달	리뷰".split("\t")
    file.to_excel("seoul_{}.xlsx".format(i))
'''

'''
서울시 자치구 리뷰 하나로 합치기
file = pd.read_excel("seoul_1.xlsx")
for i in range(2, 26):
    new = pd.read_excel("seoul_{}.xlsx".format(i))
    file = pd.concat([file, new])

file.to_excel("seoul_total.xlsx")
print(file.info)
'''

df = pd.read_excel("seoul_total.xlsx")
df.reset_index()
df.drop(['Unnamed: 0', "Unnamed: 0.1"], axis=1, inplace=True)
df.drop_duplicates(['브랜드', '일자', '주문메뉴', '리뷰'])
df.to_excel("new.xlsx")

location = df['자치구'].str.split(' ') # 문자열을 split 메소드로 분리
fran = df['브랜드'].str.split("-")
df['시'] = location.str.get(0)
df['구'] = location.str.get(1)
df['동'] = location.str.get(2)
df['도로명'] = location.str.get(3)
df.drop(['시', "동", "도로명"], axis=1, inplace=True)

# result = Counter(myList)
# for key in result:
#     print key, result[key]