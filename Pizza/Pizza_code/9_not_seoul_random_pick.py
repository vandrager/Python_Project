import os, re, usecsv
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")

df = pd.read_csv("아파트(매매)__실거래가_20210105153210.csv", encoding="cp949")

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
location = df['시군구'].str.split(' ') # 문자열을 split 메소드로 분리
df['시'] = location.str.get(0)
df['군'] = location.str.get(1)
df['구'] = location.str.get(2)


# list_loc = df.drop_duplicates(subset=['시'], inplace = True) # 시 중복값 제거
# 중복값 제거 위한 전처리
df['시군'] = df['시'] + " " + df['군']
df[df['시'] == "서울특별시"] = np.nan

# 랜덤 주소 추출을 위한 shuffle 적용
df_shuffled = df.iloc[np.random.permutation(df.index)].reset_index(drop=True)
df_shuffled.drop_duplicates(subset=['시군'], inplace = True) # 시군 중복값 제거
df_shuffled.dropna(axis = 0, inplace= True) # 서울특별시 주소 정보 제거
df_shuffled['주소'] = df_shuffled['시군'] + " " + df_shuffled['도로명']# 웹스크래핑에 사용할 주소 열 생성
data = df_shuffled.loc[:, "주소"].head(25) # 인덱스와 주소만 가져와 별도의 데이터 프레임 생성, 랜덤으로 추출 상위 25개 불러오기

# 자동완성 안되는 주소는 임의로 주소 입력해주기: 2건
print(data)
print(len(data))


# 원하는 폴더에 seoul_random.csv 파일 저장 완료
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
data.to_csv("not_seoul_random.csv", encoding = "cp949")