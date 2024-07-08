# 셀레니움 드라이버 임포토
import selenium 

# 웹드라이버 임포트
from selenium import webdriver

# time  임포트
import time

# 크롬 창 크기를 최대화 한다
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('chromedriver.exe',chrome_options=options)
