# SMTP 라이브러리를 이용하여 메일을 보내보자.
# 이걸 왜쓰나?
# 크롤러 돌리는데 오래걸리는데 끝나고 메일 보내라고 하면 편하다.

# SMTP 서버를 빌려서 쓰자.

import smtplib
from email.mime.text import MIMEText 

from email.mime.multipart import MIMEMultipart # 메일 꾸미기

from email import encoders
from email.mime.base import MIMEBase # 첨부파일 넣기


#HTML을 써서 메일 꾸미기 가능 
msg = MIMEMultipart('alternative')
내용 = """
<h4>엄태성입니다.</h4>
<button>눌러주세요</button>
"""
part1 = MIMEText(내용, "html")
msg.attach(part1)


# text = "SMTP 연습"
# msg = MIMEText(text) 

# 첨부파일을 넣어보자.
with open(r'C:\Users\taeseong\Desktop\파이썬\Crawling\Part3\Pillow\new_photo1.jpg', 'rb') as 파일:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(파일.read())

#파일 base64 인코딩
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="new_photo1.jpg"')
msg.attach(part)


 
msg['Subject'] ="이 메일은 SMTP로 보내졌습니다."
msg['From'] = 'djaxotjd95@naver.com'
msg['To'] = '엄태성'
print(msg.as_string())
 
s = smtplib.SMTP_SSL('smtp.naver.com' , 465 ) 
s.login( 'djaxotjd95' , '??????' ) #네이버로그인
s.sendmail( 'djaxotjd95@naver.com', '6380714@gmail.com', msg.as_string() )
s.close()