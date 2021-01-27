import re
import pandas as pd
'''
remove_text = 'asdf(bsde(18))'
my_regex = "\(.*\)|\s-\s.*"
remove_text = re.sub(my_regex, '', remove_text)
print(remove_text)

text  = "서울핫도그피자 remon".split(" ")
print(text)

df = pd.DataFrame([["asdf(bsde(18))", 2, 3],
                    ["aecf(bsde(18))", 2, 3],
                    ["awvf(bsde(18))", 2, 3]],
                    columns = ["브랜드", "키", "몸무게"])

for i in range(len(df)):
    df['브랜드'][i] = re.sub(my_regex, '', df['브랜드'][i])
    print(df['브랜드'][i])

print(re.sub(my_regex, '', df['브랜드'][0]))
print(type(df['브랜드'][0]))
'''

content = 'The          mountain brown       fox jumps   over  the  lazy dog'
mail = ' '.join(content.split())
print(mail)
