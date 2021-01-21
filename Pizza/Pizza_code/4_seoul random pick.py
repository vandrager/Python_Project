import os, re, usecsv
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")

df = pd.read_csv("아파트(매매)__실거래가_20210105153210.csv", encoding="cp949")
print(df.head())
'''
           시군구   번지   본번  부번   단지명      면적    계약년월  계약일    거래금액   층  건축년도          도로명
0  강원도 강릉시 견소동  202  202   0  송정한신  84.945  202012    3  17,000  13  1997  경강로2539번길 8
1  강원도 강릉시 견소동  202  202   0  송정한신  59.800  202012    5  13,800   7  1997  경강로2539번길 8
2  강원도 강릉시 견소동  202  202   0  송정한신  84.945  202012    9  18,000  13  1997  경강로2539번길 8
3  강원도 강릉시 견소동  202  202   0  송정한신  39.080  202012   11  10,000  13  1997  경강로2539번길 8
4  강원도 강릉시 견소동  202  202   0  송정한신  59.800  202012   11  12,800   3  1997  경강로2539번길 8
'''

location = df['시군구'].str.split(' ') # 문자열을 split 메소드로 분리

df['시'] = location.str.get(0)
df['군'] = location.str.get(1)
df['구'] = location.str.get(2)
# 서울특별시 + (강남구, 종로구, 동작구, 도봉구...)
df['시구'] = df['시'] + " " + df['군']
df[df['시'] != "서울특별시"] = np.nan
df.drop_duplicates(subset=['시군구'], inplace = True) # 시군구 중복값 제거
df.drop_duplicates(subset=['시구'], inplace = True) # 시구 중복값 제거
df.dropna(axis = 0, inplace= True)
df['주소'] = df['시군구'] + " " + df['도로명'] # 웹스크래핑에 사용할 주소 열 생성
data = df.loc[:, "주소"] # 인덱스와 주소만 가져와 별도의 데이터 프레임 생성

# 자동완성 안되는 주소는 임의로 주소 입력해주기: 2건
data.loc[42672] = "서울특별시 동작구 상도동 414 건영아파트" 
data.loc[44530] = "서울특별시 종로구 견지동 110 종로1가 대성 스카이렉스"
print(data)
print(len(data))
'''
C:\Python39\lib\site-packages\pandas\core\indexing.py:670: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
'''
'''
40653                서울특별시 강남구 개포동 언주로 3
40956          서울특별시 강동구 강일동 아리수로93가길 25
41163           서울특별시 강북구 미아동 오패산로30길 30
41248               서울특별시 강서구 가양동 허준로 47
41422        서울특별시 관악구 남현동 남부순환로260길 119
41555           서울특별시 광진구 광장동 아차산로76길 31
41616         서울특별시 구로구 개봉동 개봉로2길 133-15
41851           서울특별시 금천구 가산동 가산로9길 12-8
41924         서울특별시 노원구 공릉동 동일로173가길 145
42323        서울특별시 도봉구 도봉동 도봉로181길 74-30
42517         서울특별시 동대문구 답십리동 답십리로41길 33
42672            서울특별시 동작구 상도동 414 건영아파트
42813           서울특별시 마포구 공덕동 마포대로 115-8
42955            서울특별시 서대문구 남가좌동 증가로 150
43085             서울특별시 서초구 내곡동 헌릉로8길 58
43335           서울특별시 성동구 금호동1가 독서당로 343
43495              서울특별시 성북구 길음동 길음로 119
43655              서울특별시 송파구 가락동 오금로 396
43932          서울특별시 양천구 목동 목동중앙본로28길 10
44114           서울특별시 영등포구 당산동 버드나루로 130
44306               서울특별시 용산구 도원동 새창로 70
44403            서울특별시 은평구 갈현동 갈현로29길 61
44530    서울특별시 종로구 견지동 110 종로1가 대성 스카이렉스
44571            서울특별시 중구 만리동1가 만리재로 193
44612              서울특별시 중랑구 망우동 상봉로 110
Name: 주소, dtype: object
'''
# 원하는 폴더에 seoul_random.csv 파일 저장 완료
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
data.to_csv("seoul_random.csv", encoding = "cp949")