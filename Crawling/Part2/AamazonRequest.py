# 아마존은 크롤링이 더욱 힘든데 뚫어보자

import requests

hd ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
} # 네트워크의 user-agent를 헤더로 붙여서 사용하자

쿠키 ={
    'session-id-time':'2082787201l', 
    'i18n-prefs':'USD',
    'sp-cdn':'L5Z9:KR', 
    'skin':'noskin', 
    'session-id':'141-9679786-4286565', 
    'ubid-main':'133-4566738-7659404',
    'session-token':'pQDD7lbBszQzVdZhfMzQ2mX7c4pC9D2qCIOuISkn27ZTTcpMJxFIWUJqawyFctvEW9502F8z++G1ymBHqfi6WmeUgn4Z0d09/R1p5fErSe0IHoZiW4xnqOxI/XkKA9c9NsWGbQFxoFkSZBpwag3pOVQ8/5iOa9IAucPQF1BFU4+9D8w1AvVXQ79U1wJ40EhnycTJiE+rnA1P+LM0DcAYM5ZV9cDoXwroG5lBZ0x0Mn6H7LvZEHR8P5tN33tCQ0sqd5mq3j6gFH8Yt/CndFrpCzRdLfgA30rq81wYY1pbVBz+LSJtilJN+/VJrYO1xcaqfZLt+m6n0BRfT/iTMFTlhUn3dEKcjyIP',
    'csm-hit':'tb:EWV3BJKATCMA0PJC7SH6+s-P1WHH3EFNEWAA5YJKJPZ|1705070035972&t:1705070035972&adb:adblk_no'
}
r = requests.get('https://www.amazon.com/s?k=monitor&crid=2Z93YR3GOMZ1D&sprefix=monitor%2Caps%2C260&ref=nb_sb_noss_1', headers=hd, cookies=쿠키)
print(r.content)
print(r.status_code) # 503으로 차단됨
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content,'lxml')
print(soup.select('.a-size-medium')[0])
# header만 했을땐 차단되었는데 쿠키도 넣으니 뚫림.


# 크롤링이 막혀 코드가 멈추는 것을 막는부분
# if r.status_code == 200:
#     print(soup.select('.a-size-medium')[0])
# else:
#     print("에러")

# try:
#     print(soup.select('.a-size-medium')[0])
# except:
#     print("에러")
