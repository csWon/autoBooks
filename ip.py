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

# 크롬드라이버 자동 설치
# chromedriver_autoinstaller.install()

# ip 메모장에서 유동프록시 아이피 불러오기

options = webdriver.ChromeOptions()
# options.add_argument('window-size=1920,1080')

prx = open('ip.txt', 'r').read().split('\n')

# 프록시 랜덤 선택
PROXY = random.choice(prx)

# 선택된 아이피 프린트
print(PROXY)

# 아이피 적용
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL"
}

#크롬 창 실행
driver = webdriver.Chrome()
driver.implicitly_wait(5)

#url 입력 받기
# urlurl = input('url 입력 : ')
# urlurl = 'https://ko.infobyip.com/'
urlurl = 'https://product.kyobobook.co.kr/'

#해당 url으로 접속
# driver.get(url=r'{}'.format(urlurl))
driver.get(urlurl)

#임시 꺼짐 방지
time.sleep(9999)

# 61.98.204.203

# 122.42.140.231
# '121.126.153.6:7279'
# 122.42.140.231
# '121.126.38.169:7483'
# '124.198.7.5:5140'