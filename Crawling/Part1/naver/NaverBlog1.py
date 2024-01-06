# 데이터를 읽어올때 페이지가 나눠진 경우는 url을 분석하여 크롤링하면 된다
# 그런데 무한으로 계속 나오는 페이지는 어떻게 할까?
# 데이터를 읽어오면 원래는 첫 화면에 있는 데이터만 가져오는데 추가데이터를 서버에 요청해야한다.

# 검사 > 네트워크 에 들어가면 페이지를 구성하기 위한 데이터를 가져오는걸 볼 수 있다.
# 새로운 데이터를 검색하여 Header를 분석하면 된다.
import requests
from bs4 import BeautifulSoup

#첫번쨰 추가 요청
requests.get('https://s.search.naver.com/p/review/46/search.naver?where=view&api_type=11&start=61&query=%EC%82%AC%EA%B3%BC&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&ac=1&aq=0&spq=0&nx_search_query=&nx_and_query=&nx_sub_query=&prank=63&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=09380110&fgn_region=&fgn_city=&lgl_lat=37.584306&lgl_long=126.90704&abt=&_callback=viewMoreContents')

#두번째 추가 요청
requests.get('https://s.search.naver.com/p/review/46/search.naver?where=view&api_type=11&start=121&query=%EC%82%AC%EA%B3%BC&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&ac=1&aq=0&spq=0&nx_search_query=&nx_and_query=&nx_sub_query=&prank=123&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=09380110&fgn_region=&fgn_city=&lgl_lat=37.584306&lgl_long=126.90704&abt=&_callback=viewMoreContents')

#이제 두 URL의 차이를 찾으면 되겠다.
# start가 61, 121로 차이가 난다. 이걸 바꾸면 되겠다