# 이미지를 압축해보자.
# pillow를 사용할거임 pip install Pillow

from PIL import Image
import os

img = Image.open('images/photo1.jpg')
# img = img.resize((300,500)) # 명시된 크기로 그냥 짜부시킴
img.thumbnail((300,500)) # 비율 그대로 압축함

img = img.crop((50,50, 150,150)).convert('L')# 왼쪽 좌표, 오른쪽 좌표만큼 짜름 convert('L')로 흑백 변환가능
img.save('new_photo1.jpg', quality=95) # 이 이름으로 저장됨. 퀄리티로 화질 정하면 됨. 기본 75

경로 = os.getcwd()
파일들 = os.listdir(경로 + '/images')
print(파일들)
 
for i in 파일들:
    img = Image.open(f'images/{i}')
    img.thumbnail((500,2500)) 
    img.save(f'new_{i}')
