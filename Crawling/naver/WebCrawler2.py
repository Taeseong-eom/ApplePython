import requests
from bs4 import BeautifulSoup

데이터 = requests.get("https://finance.naver.com/item/sise.nhn?code=005930")
soup = BeautifulSoup(데이터.content, 'html.parser')

# 1. 글자가 여러개로 나눠져 있는 경우 바로 위에껄 읽으면 된다.
print(soup.find_all('em', class_="X")[0].text)



# CSS 셀렉터를 입력해서 원하는 HTML 찾기 가능
# EX) soup.select('.f_up') # .(클래스) --> class 명이 f_up인걸 찾아라
# EX) soup.select('strong#f_up') # .(클래스) --> strong인데 id가 f_up인걸 찾아라. 물론 strong 안써도 됨



# 2. class, id가 없는 요소인 경우 -> select()룰 쓰면 됨
# 또한 내부 요소를 찾을 땐 띄어쓰기를 쓰면 됨
print(soup.select('.gray .f_up em')[0].text)
# #tab_con1 > div:nth-child(6) > table > tbody > tr:nth-child(2) > td > em   // 우클릭해서 copy select 하면 더 정확하긴함


# 3. 이미지 수집하기
이미지 = soup.select('#img_chart_area')[0]
print(이미지['src']) # 이렇게 src만 출력할 수도 있다.



# 4. 다른 정보도 같이 수집하기
데이터 = requests.get("https://finance.naver.com/item/main.naver?code=066570")  # URL 뒷부분만 수정하면 여러 페이지 데이터를 가져올 수 있겠다.
soup = BeautifulSoup(데이터.content, 'html.parser')
print(soup.select('#chart_area > div.rate_info > div > p.no_today > em')[0].text)


