# 서울 전 지역 데이터 통합
# 1. 추출한 엑셀파일을 불러와 concat으로 합친다.
# 2. 지점 중복이 있을 수 있으므로 지점을 기준으로 중복값을 제거한다.
# df.drop_duplicates(subset=['지점'], inplace = True)
# 3. 중복을 제외한 자치구, 지점명만 가져와 하나의 데이터 프레임으로 만들어준다.
# line = df.loc[:,  ["자치구", "지점"]]
import pandas as pd
import os
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")

for i in range(1, 5):
    file = pd.read_excel("seoul_{}.xlsx".format(i), encoding = "cp949")
    dataset = pd.concat(dataset, file)
# df.drop_duplicates(['지점', '주문메뉴', '주문일', '코멘트'])
print(dataset.info)
from collections import Counter # Counter: 리스트에서 모든 아이템을 count 하고 싶을 때 사용
# result = Counter(myList)
# for key in result:
#     print key, result[key]