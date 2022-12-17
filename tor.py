from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import os
import inspect, os, platform, time, random, sys
from datetime import datetime, timedelta
import chromedriver_autoinstaller
import subprocess
import os
# os.system('"C:/Windows/System32/notepad.exe"')
# os.system('"C:/test.txt"')

# os.system('"C:/test.txt"')
os.system('"C:/Users/c.won/Desktop/Tor Browser/Browser/test.txt"')
os.system('"C:/Users/c.won/Desktop/Tor Browser/Browser/firefox.exe"')
# subprocess.call([r'"C:/test.txt"'])
# subprocess.call(['C:/Users/c.won/Desktop/Tor\ Browser/Browser/test.txt'])
#                 C:\Users\c.won\Desktop\Tor Browser\Browsera
#크롬드라이버 자동 설치
chromedriver_autoinstaller.install()
# os.system('"' + self.filePath + '"')
# torPath = r'C:\Users\c.won\Desktop\Tor Browser\Browser\firefox.exe'
# torexe = os.popen('"'+torPath+'"')
# os.system('"C:\\Users\\My Name\\Desktop\\Tor Browser\\Browser\\firefox.exe"' )
os.system('"C:\\Users\\My Name\\Desktop\\Tor Browser\\Browser\\test.txt"' )
#아이피 적용
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=socks5://127.0.0.1:9150")

#크롬 창 실행
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

#url 입력 받기
urlurl = 'https://www.naver.com'

#해당 url으로 접속
driver.get(url=r'{}'.format(urlurl))

#임시 꺼짐 방지
time.sleep(9999)

