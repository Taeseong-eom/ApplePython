# 일단 pip install requests, pip install bs4 하자
# pip를 통해 라이브러리 설치
# 라이브러리란 ? 남이 만들어놓은 코드 사용

import requests # 파이썬으로 웹사이트 접속을 도와주는 라이브러리
from bs4 import BeautifulSoup # HTML웹문서 분석을 도와주는 라이브러리
#이게 크롤러의 기본임

# 크롤러 진행 과정
# 1. 파이썬으로 데이터가 있는 웹사이트에 접속
데이터 = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')
# print(데이터.status_code) # 200 뜨면 잘 온거임
# print(데이터.content) # URL에 있는 모든 HTML 데이터가 나옴


# 근데 깨져서 나오는데 이걸 해결해보자
soup = BeautifulSoup(데이터.content, 'html.parser') # 이뻐진 html
# print(soup.find_all('태그명', '속성명')) 이렇게 찾을 수 있음
print(soup.find_all('strong', id="_nowVal")[0].text) # 찾은 데이터를 리스트[]로 반환함.
# [0] 첫번째 리스트에서 데이터만 읽으려면.text하면 됨

# id가 아닌 class로도 찾을 수 있는데 class는 예약어라서 뒤에 _를 붙여야함.
# class뒤에 여러 클래스가 있는데 띄어쓰기로 구분되어 있어서 하나만 쓰면 됨.
# class="tah p11 nv01"
print(soup.find_all('span', class_="tah")[0].text)

# 또한 id는 유니크해서 중복되지 않는데 class는 중복되어 여러값이 들어 있을 수 있음




# 2. HTML을 받아서 원하는 정보 뽑는다


