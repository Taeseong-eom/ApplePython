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




driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://instagram.com') # 드라이버에는 사이트에 관한 모든 정보가 들어가게 됨
time.sleep(5) # 5초 정지(페이지 뜨는데 시간이 걸려서 기다림)

# e = driver.find_element(By.CLASS_NAME, '_ap3a').text
# print(e)# 가입하기 글자 출력완.

# e = driver.find_element(By.CLASS_NAME, 'x9f619').text
# print(e)# 로그인 글자?


# e = driver.find_element(By.NAME, 'username').text
# print(e)


#인스타그램 자동로그인 해보자
e = driver.find_element(By.NAME, 'username') # 여기에 아이디 입력할 거임
e.send_keys('djaxotjd95@naver.com')
e = driver.find_element(By.NAME, 'password') # 여기에 비밀번호 입력할 거임
e.send_keys('비밀번호')
e.send_keys(Keys.ENTER) # 이렇게 엔터도 칠 수 있음

time.sleep(1000000) #코드 맨 마지막에 추가/ 자동 종료 방지