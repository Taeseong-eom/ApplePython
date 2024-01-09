# 단순반복 웹작업, 구조가 어려운 사이트 크롤링할 때 도움이 되는 selenium

# selenium, chromdriver 를 다운해야한다.
# chrome://version 입력 후 버전에 맞는 크롬드라이버 다운]
# 그리고 pip install selenium 하자.




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager #드라이버 대신에 사용(자동 업데이트)
from selenium.webdriver.common.by import By

import urllib.request


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://instagram.com') # 드라이버에는 사이트에 관한 모든 정보가 들어가게 됨
# time.sleep(3) # 5초 정지(페이지 뜨는데 시간이 걸려서 기다림)
driver.implicitly_wait(10)

# e = driver.find_element(By.CLASS_NAME, '_ap3a').text
# print(e)# 가입하기 글자 출력완.

# e = driver.find_element(By.CLASS_NAME, 'x9f619').text
# print(e)# 로그인 글자?


# e = driver.find_element(By.NAME, 'username').text
# print(e)


#인스타그램 자동로그인 해보자
e = driver.find_element(By.NAME, 'username') # 여기에 아이디 입력할 거임
e.send_keys('6380714@mju.ac.kr')
e = driver.find_element(By.NAME, 'password') # 여기에 비밀번호 입력할 거임
e.send_keys('??????') # 깃허브에 올릴거라서 가림
e.send_keys(Keys.ENTER) # 이렇게 엔터도 칠 수 있음

time.sleep(5)

#이제 페이지 이동하여 사진을 저장할 것이다.   
driver.get('https://www.instagram.com/explore/tags/%EC%82%AC%EA%B3%BC/') # 이렇게 하면 페이지 이동함.

driver.implicitly_wait(10) #요소가 없으면 최대 10초간 기다려라.

e = driver.find_element(By.CLASS_NAME, '_aagw').click() # s면 여러개 찾아서 리스트로 만듬.[]

driver.implicitly_wait(10)

# 이미지 = driver.find_element(By.CSS_SELECTOR, '._aa20 ._aagv > img').get_attribute('src') #src를 가져와서 저장.
# urllib.request.urlretrieve(이미지,'1.jpg') 

# driver.find_elements(By.CSS_SELECTOR, '._abl-')[0].click() # 가끔 클릭이 안되면
# # driver.excute_script('argumnets[0].click();'m e) 이러면 클릭됨

# # 두번째 사진 저장할때 class가 중복되어 같은 사진이 저장되는 문제 발생.
# # 상위 class가 유니크한것을 명시하면 된다.

# time.sleep(1)


# 이미지 = driver.find_element(By.CSS_SELECTOR, '._aa20 ._aagv > img').get_attribute('src') #src를 가져와서 저장.
# urllib.request.urlretrieve(이미지,'2.jpg') 

# body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div:nth-child(1) > div > div > div > button
# body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div:nth-child(1) > div > div > div._aaqg._aaqh > button
# body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div:nth-child(1) > div > div > div._aaqf._aaqh > button

#그럼 이걸 반복해보자
for i in range(50):
    이미지 = driver.find_element(By.CSS_SELECTOR, '._acay ._aagv > img').get_attribute('src') #src를 가져와서 저장.
    urllib.request.urlretrieve(이미지, f'{i}.jpg') 
    driver.implicitly_wait(10)    
    driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-').click()
    driver.implicitly_wait(10)


time.sleep(1000000) #코드 맨 마지막에 추가/ 자동 종료 방지

