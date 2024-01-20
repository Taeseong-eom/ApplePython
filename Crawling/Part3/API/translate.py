from papago import 번역기 # from 파일명 import 함수명// from 하위폴더명/파일명 import 함수명,함수명2, ... or *
import pandas as pd
# openpyxl 있어야 엑셀 열 수 있음

data = pd.read_excel('english.xlsx', engine='openpyxl') # engine='openpyxl' 해야 제대로 열 수 있음


# 데이터가 많으면 itertuple을 쓰자- > 더빠름
for l, row in data.iterrows(): # 가로줄 하나씩 반복가능 / l은 행번호, row는 내용
    # row['korean'] = 번역기(row['english'])
    data.loc[l, 'korean'] = 번역기(row['english'])
    # pandas로 연 데이터프레임 수정시 data.loc[행,열] 으로 하자.

print(data)

data.to_excel('output.xlsx')