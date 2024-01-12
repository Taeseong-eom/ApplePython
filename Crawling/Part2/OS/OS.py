import os

#os 라이브러리를 이용하여 여러 파일을 조작해보자



# 파일명 변경을 해보자
#os.rename('기존파일명', '새파일명')
# os.rename('test/1.txt', 'test/1.1.txt')
 
# 모든 파일을 변경하고 싶다면
for i in os.listdir('test'):
    os.rename(f'test/{i}', f'test/a{i}')





파일 = os.listdir('test') # 이 경로에 있는 파일 다 가져와

# 파일 복사는 어떻게 할까
import shutil
# shutil.copy('파일명','파일명')

for i in os.listdir('test'):
    
    shutil.copy(f'test/{i}',f'test2/{i}')
    # 대량 파일 복사 성공

# 절대경로를 복붙할때는 r(row)를 붙여야함

#경로 합치기    
# os.path.join('경로1','경로2')
# 경로1/경로2 으로 나옴 + 써도 되지만 오래된 파이썬인 경우엔 안되는 경우도 있음
# os.getcwd() 현재 파일 경로