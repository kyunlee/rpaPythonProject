import pyautogui as p 
import time
import selenium # 여기서는 약자를 붙이지 않았다.
from selenium import webdriver

#time.sleep(2) # 2초간 인터벌을 인위적으로 부여한다.
#p.position() # 현재 x축과 y축의 좌표

#Point(x = 1379, y= 97)

#p.onScreen(300, 300)
#p.moveTo(300, 300, duration=1)
 
#p.alert(text='확인되엇습니다.', title = '인증', button='Ok')

dirver = webdriver.Chrome('chromedriver.exe')
