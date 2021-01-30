import os
import pandas as pd
import numpy as np

menu = ['베이컨', '고르곤졸라', '치즈', '콤비네이션', '스테이크', '쉬림프', '포테이토', '치킨', '고구마', '불고기', '하와이안', '페페로니'] # 없으면 기타로 구분한다.
group = ['Single', 'Side', 'Party']
brand = ['피자헛', '파파존스', '도미노피자', '반올림피자샵', '미스터피자', '피자마루', '피자알볼로', '피자나라치킨공주', '7번가피자', '피자헤븐']

'''
# 추천시스템 고객 IN/OUT 구분
[INPUT]
# Step. 0 당신이 원하는 추천은?
- 옵션선택 ver(맞춤추천) / 베스트 ver(인기 베스트순 - 일자별 데이터 추천 지수 반영)

# Step. 1 평소 당신의 피자 취향은?
- 다중선택 가능!
menu = ['베이컨', '고르곤졸라', '치즈', '콤비네이션', '스테이크', '쉬림프', '포테이토', '치킨', '고구마', '불고기', '하와이안', '페페로니']

# Step. 2 원하는 양은 어느 정도?
- 'Single': 다른거 다 필요없이 피자 한 판만 주문
- 'Side': 약간 아쉬우니까 소스랑 사이드 메뉴도 주문
- 'Party': 오늘은 돼지파티, 세트로 양 넉넉하게 주문
group = ['Single', 'Side', 'Party']

# Step. 3 평소 좋아하는 브랜드는 어디?
- 좋아하는 브랜드를 선택해주세요!
brand = ['피자헛', '파파존스', '도미노피자', '반올림피자샵', '미스터피자', '피자마루', '피자알볼로', '피자나라치킨공주', '7번가피자', '피자헤븐']


# 메뉴 구분 정의
메뉴 구분은 워드클라우드 데이터 분석을 통해 주요 리스트 추출
메뉴 리스트의 키워드가 포함되었다면 메뉴구분열에 해당키워드를 추가할 것 ex) 이탈리안쉬림프피자 -> 쉬림프 

# 그룹 구분 정의
주문메뉴를 봤을 때
세트 no, menu2 false -> 단품 (Single, O)
세트 no, menu2 true  & menu3 false -> 사이드 (Side, O)
세트 yes or menu 3 True -> 파티 (Party, O)

파티(15만) > 사이드(16만) > 단품(26만)

Single: only menu1
Side: only menu1
Party: menu len 4

'''

# 데이터 전처리 테스트
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
file = pd.read_excel("test.xlsx")
df = file.copy()

for i in range(len(df)):
    df['메인메뉴'][i] = df['메인메뉴'][i].replace("R/1", "")
    df['메인메뉴'][i] = df['메인메뉴'][i].replace("L/1", "")
    # df['메인메뉴'][i] = df['메인메뉴'][i].replace("(R)", "")
    # df['메인메뉴'][i] = df['메인메뉴'][i].replace("(L)", "")


# 데이터 전처리 작업 실행 ( 메뉴 )
df['메뉴구분'] = ""
for i in range(len(df)):
    for k in menu:
        if k in df['메인메뉴'][i]:
            df['메뉴구분'][i] += k
    if df['메뉴구분'][i] == "":
        df['메뉴구분'][i] = "기타"


# 데이터 전처리 작업 실행 ( 그룹 )
print(df['메인메뉴'])
print(df['메뉴2'])
df['그룹구분'] = "plz success"
set_list = ['SET', '세트', 'set']

for j in range(len(df)):
    if df['메뉴2'][j] == np.nan:
        df['그룹구분'][j] = "Single"
    
print(df['메뉴구분'])
print(df['그룹구분'])


# df = pd.DataFrame([["", "김", 3],
#                     ["", "이", 3],
#                     ["", "이", 3],
#                     ["", "이", 3],
#                     ["", "이", 3],
#                     ["", "이", 3],
#                     ["", "이", 3],
#                     ["", "박", 3]],
#                     columns = ["브랜드", "키", "몸무게"])

# for i in range(len(df)):
#     print(df['키'][i][-1])

# print(df.info())