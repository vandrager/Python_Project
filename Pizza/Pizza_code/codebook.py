import os
import pandas as pd
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")


df = pd.read_excel("test.xlsx")
print(df)

# 워드클라우드를 통해 주문 메뉴 리스트 추출
# 브랜드별로 페페로니 페퍼로니 메뉴명이 다름 페페로니로 전처리 필요함
menu = ['베이컨', '고르곤졸라', '치즈', '콤비네이션', '스테이크', '쉬림프', '포테이토', '치킨', '고구마', '불고기', '하와이안', '페페로니'] # 없으면 기타로 구분
group = ['Single', 'Set', 'Side', 'Party']
brand = ['피자헛', '파파존스', '도미노피자', '반올림피자샵', '미스터피자', '피자마루', '피자알볼로', '피자나라치킨공주', '7번가피자', '피자헤븐']

'''
고객 선택 구분
그룹과 브랜드는 필수, 메뉴는 선택사항으로 지정

# 메뉴 구분 정의
메뉴 리스트의 키워드가 포함되었다면 메뉴구분열에 해당키워드를 추가할 것 ex) 이탈리안쉬림프피자 -> 쉬림프 

# 그룹 구분 정의
주문메뉴를 봤을 때
추가no 세트no, menu2 false -> 단품
추가 yes, 세트 no menu2 true -> 사이드
세트 yes -> 세트
menu4 True -> 파티

길이 수 구분, 데이터 검증
세트 파티 사이드 단품
메뉴 성향은 키워드 분석 주로 나오는 키워드 정리해서 리스트 추출

Single: only menu1
Set: only menu1
Side: only menu1
Party: menu len 4

'''


'''
# 데이터 전처리 작업 실행 ( 메뉴 )
df['메뉴구분'] = ""
for i in range(len(df)):
    for k in menu:
        if k in df['메인메뉴'][i]:
            df['메뉴구분'][i] += k
    if df['메뉴구분'][i] == "":
        df['메뉴구분'][i] = "기타"




# 데이터 전처리 작업 실행 ( 그룹 )
df['그룹구분'] = ""
set_list = ['SET', '세트', 'set']
for i in range(len(df)):
    if df['주문메뉴'][i] in set_list:
        df['그룹구분'] = "Set"
    elif df['메뉴4'][i] == True:
        df['그룹구분'] = "Party"
    elif df['메뉴2'][i] == True:
        df['그룹구분'] = "Side"
    elif df['메뉴2'][i] == False:
        df['그룹구분'] = "Single"
    
print(df['메뉴구분'])
print(df['그룹구분'])
'''

df = pd.DataFrame([["asdf(q3de(18)), ( england 2020 )", "김", 3],
                    ["aecf(bwe(34))/ ( korea( 2020 ))", "이", 3],
                    ["nwvf(bsde(6g)) - (china(2020)", "박", 3]],
                    columns = ["브랜드", "키", "몸무게"])

for i in range(len(df)):
    print(df['키'][i][-1])