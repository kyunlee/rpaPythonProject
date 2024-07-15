import pyautogui as p # as 뒤는 약자이다.
import time

time.sleep(2) # 2초간 인터벌을 인위적으로 부여한다.
p.position() #현재 x축과 y축의 좌표

#Point(x = 1379, y=97)

#p.size() # 현재 x축과 y축의 좌표
#Point(width = 1920, height = 1080)

p.onScreen(300, 300)
True