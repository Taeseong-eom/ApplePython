import pandas as pd
import re
# pip install openpyxl 해줘야함.

raw = pd.read_excel(r'C:\Users\taeseong\Desktop\파이썬\Crawling\Part3\Pandas\product.xlsx', engine='openpyxl')
print(raw)

# 기존 엑셀에 가격에 부가세 10%를 더한 가격을 추가해보자.
raw['부가세포함가격'] = raw['판매가'] * 1.1
# print(raw)

# apply쓰면 (함수)안에 raw 데이터를 하나하나 전부 함수안에 넣었다가 뻄
# def 함수(data):
#     return 1.1*data

# new_raw = raw['판매가'].apply(함수)
# print(new_raw)

# 정규식을 써서 글자에 원하는 글자가 있는지 확인. regex
# pandas로 읽은애는 object라서 안됨 그래서 str로 변환
def 함수2(data):
    if re.search('Chair', str(data)):
        return "의자"
    elif re.search('Sofa', str(data)):
        return "소파"
    else:
        return "기타"

raw['카테고리'] = raw['상품목록'].apply(함수2)
print(raw)