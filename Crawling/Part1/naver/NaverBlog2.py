import requests
from bs4 import BeautifulSoup

data = requests.get('https://s.search.naver.com/p/review/46/search.naver?where=view&api_type=11&start=121&query=%EC%82%AC%EA%B3%BC&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&ac=1&aq=0&spq=0&nx_search_query=&nx_and_query=&nx_sub_query=&prank=123&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=09380110&fgn_region=&fgn_city=&lgl_lat=37.584306&lgl_long=126.90704&abt=&_callback=viewMoreContents')

soup = BeautifulSoup(data.text.replace('\\',''), 'html.parser')# 이런식으로 \를 ''바꿔줘야한다.
# 또한 replace는 문자만 바꿀 수 있다. 그래서 text로 바꿔서 변경해준다.

# findall이나 select를 써서 수집하는데 데이터에 \가 있는 경우 제대로 수집이 안됨
# 그래서 \를 제거해줘야함.

리스트 = soup.select('a.title_link')
print(리스트[0].text)
print(리스트[1].text)




# body > li:nth-child(1) > div > div.\\\"detail_box\\\" > div.\\\"title_area\\\" > a