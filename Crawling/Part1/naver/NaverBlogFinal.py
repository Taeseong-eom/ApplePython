# 검색어 입력받고 입력값에 대한 네이버블로그제목 100개 수집해보자

import requests
from bs4 import BeautifulSoup

word = input('검색어를 입력해주세요 : ')

f = open('NaverBlogFinal.txt', 'w', encoding='utf-8')
count = 0 
for i in range(1,5):
    PageFirtNum = 3 * i
    데이터 = requests.get(f'https://s.search.naver.com/p/review/46/search.naver?where=view&api_type=11&start={str(PageFirtNum + 1)}&query={word}=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&ac=1&aq=0&spq=0&nx_search_query=&nx_and_query=&nx_sub_query=&prank=33&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=09380110&fgn_region=&fgn_city=&lgl_lat=37.584306&lgl_long=126.90704&abt=&_callback=viewMoreContents')
    soup = BeautifulSoup(데이터.text.replace('\\',''), 'html.parser')
    for num in range(30):
        f.write(soup.select('a.title_link')[num].text + '\n')
        count = count + 1
        print(soup.select('a.title_link')[num].text + " : " + str(count) + '\n') # 잘되는지 테스트 출력
        if count >= 100:
            break
f.close()

