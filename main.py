import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
from selenium.webdriver.chrome.options import Options
# from stem import Signal
# from stem.control import Controller
import inspect, os, platform, time, random, sys
import time
# from stem import Signal
# from stem.control import Controller
from selenium import webdriver
import chromedriver_autoinstaller
from datetime import datetime
import logging

url_ip_check = 'https://ko.infobyip.com/'
url_k_product = 'https://product.kyobobook.co.kr/'
url_naver = 'https://www.naver.com'
url_aladin = 'https://www.aladin.co.kr/'
url_ypbook = 'https://www.ypbooks.co.kr/'


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

#크롬드라이버 자동 설치
chromedriver_autoinstaller.install()



def getTorDriver():
    # os.system('"C:\\Users\\My Name\\Desktop\\Tor Browser\\Browser\\firefox.exe"')
    os.system('"C:\\Users\\My Name\\Desktop\\Tor Browser\\Browser\\test.txt"')
    # 아이피 적용
    options = webdriver.ChromeOptions()
    options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disavle-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #크롬 창 실행
    driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(5)

    return driver



def delay():
    time.sleep(3)
    # wait_time = random.uniform(15, 20)
    # driver.implicitly_wait(wait_time)
def delay_10():
    time.sleep(10)
    # wait_time = random.uniform(15, 20)
    # driver.implicitly_wait(wait_time)

def delay_n(n):
    time.sleep(n)

def get_ua():
    ua_list = [
                # 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.79 Mobile Safari/537.36',
                # 'Mozilla/5.0 (iPad; CPU OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/108.0.5359.52 Mobile/15E148 Safari/604.1',
                # 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/108.0.5359.52 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                # 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1',
                # 'Mozilla/5.0 (iPad; CPU OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
                'Mozilla/5.0 (X11; Linux i686; rv:107.0) Gecko/20100101 Firefox/107.0',
                # 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/107.0 Mobile/15E148 Safari/605.1.15',
                # 'Mozilla/5.0 (iPad; CPU OS 13_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/107.0 Mobile/15E148 Safari/605.1.15',
                # 'Mozilla/5.0 (Android 13; Mobile; rv:68.0) Gecko/68.0 Firefox/107.0',
                # 'Mozilla/5.0 (Android 13; Mobile; LG-M255; rv:107.0) Gecko/107.0 Firefox/107.0',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Mozilla/5.0 (X11; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/107.0.1418.68',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/107.0.1418.68',
                # 'Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.79 Mobile Safari/537.36 EdgA/107.0.1418.62',
                # 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.79 Mobile Safari/537.36 EdgA/107.0.1418.62',
                # 'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.79 Mobile Safari/537.36 EdgA/107.0.1418.62',
                # 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.79 Mobile Safari/537.36 EdgA/107.0.1418.62'
                ]
    ua = random.choice(ua_list)
    print(ua)
    return ua

def tor_browser():
    # torexe = os.popen(r'C:\Users\c.won\Desktop\"Tor Browser"\Browser\TorBrowser\Tor\tor.exe')
    PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT

    # 옵션 설정
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("disable-infobars")
    chrome_options.page_load_strategy = 'normal'
    chrome_options.add_argument('--enable-automation')
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('user-agent={}'.format(useragent))
    chrome_options.add_argument('--lang=ko_KR')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-browser-side-navigation')
    chrome_options.add_argument('--mute-audio')
    #    Tor 프록시 설정 (ip 우회)
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.headless = True
    # user_agent = get_ua()
    # chrome_options.add_argument('user-agent=' + user_agent)

    # 브라우저 열기
    driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe', options=chrome_options)
    # driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe', options=options)
    # driver = webdriver.Chrome()

    return driver

def open_browser_c():
    # chrome_path = '/usr/local/bin/chromedriver'
    # torexe = os.popen(r'/usr/local/bin/tor')
    # torexe = os.popen(r'/opt/homebrew/opt/tor/bin/tor')
    # PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT
    # PROXY = "socks5://127.0.0.1:9150"  # IP:PORT or HOST:PORT
    chromedriver_autoinstaller.install()

    prx = open('ip.txt', 'r').read().split('\n')

    # 프록시 랜덤 선택
    PROXY = random.choice(prx)
    print("proxy : " + PROXY)

    chrome_options = webdriver.ChromeOptions()
    # options.add_argument('window-size=1920,1080')
    # 옵션 설정
    # chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("disable-infobars")
    chrome_options.page_load_strategy = 'normal'
    chrome_options.add_argument('--enable-automation')
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('user-agent={}'.format(useragent)) # todo 설정 필요
    chrome_options.add_argument('--lang=ko_KR')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-browser-side-navigation')
    chrome_options.add_argument('--mute-audio')
    # #    # Tor 프록시 설정 (ip 우회)
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.headless = True
    user_agent = get_ua()
    chrome_options.add_argument('user-agent=' + user_agent)

    # 아이피 적용
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL"
    }

    # 브라우저 열기
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    print('------------------------------')

    return driver

def yes24(keyword, page, n):
    driver.get('http://www.yes24.com/')
    # 책 제목 입력
    # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
    search_box = driver.find_element(By.CLASS_NAME, 'iptTxt')
    search_box.click()
    # search_box.send_keys('영어회화')
    search_box.send_keys(keyword)
    delay()

    # 검색 버튼 클릭
    # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
    btn = driver.find_element(By.CLASS_NAME, 'schBtn')
    btn.click()
    delay_10()

    # 목적물 클릭
    # document.getElementsByClassName('bgYUI ico_nWin')[15].click()
    # targets = driver.find_element(By.CLASS_NAME, 'bgYUI ico_nWin')
    targets = driver.find_elements(By.CLASS_NAME, 'lnk_img')
    # targets[10].click()
    targets[22].click()
    delay_10()
    print(driver.current_url)
    print(driver.title)
    # 10 / 영어회화 / # 잡지] EBS 라디오 EASY ENGLISH 초급영어회화 (월간) : 12월 [2022] EBS 라디오 EASY ENGLISH 초급영어회화 (월간) : 12월 [2022] 새창이동
    # 23 / 영어회화 / 해커스톡 영어회화 10분의 기적 : 미국에
    # 23 / 삼국지 / 고사성어로 읽는 정사 삼국지


def yes24_v2(keyword, page, n):
    print(yes24_v2)
    print(keyword)
    print(page)
    print(n)
    driver.get('http://www.yes24.com/')

    fakeKeywords = open('keyword.txt', 'r',  encoding='UTF8').read().split('\n')
    Keyword_3 = random.choices(fakeKeywords, k=3)

    for fKeyword in Keyword_3:
        # 책 제목 입력
        # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
        search_box = driver.find_element(By.CLASS_NAME, 'iptTxt')
        search_box.click()
        search_box.send_keys(fKeyword)
        delay()

        # 검색 버튼 클릭
        # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
        btn = driver.find_element(By.CLASS_NAME, 'schBtn')
        btn.click()
        delay_10()

        driver.back()

    search_box = driver.find_element(By.CLASS_NAME, 'iptTxt')
    search_box.click()
    search_box.send_keys(keyword)
    delay()

    # 검색 버튼 클릭
    # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
    btn = driver.find_element(By.CLASS_NAME, 'schBtn')
    btn.click()
    delay_10()

    # 목적물 클릭
    # document.getElementsByClassName('bgYUI ico_nWin')[15].click()
    # targets = driver.find_element(By.CLASS_NAME, 'bgYUI ico_nWin')
    targets = driver.find_elements(By.CLASS_NAME, 'lnk_img')
    # targets[10].click()
    targets[22+n].click()
    delay_n(60)
    print(driver.current_url)
    print(driver.title)
    # 10 / 영어회화 / # 잡지] EBS 라디오 EASY ENGLISH 초급영어회화 (월간) : 12월 [2022] EBS 라디오 EASY ENGLISH 초급영어회화 (월간) : 12월 [2022] 새창이동
    # 23 / 영어회화 / 해커스톡 영어회화 10분의 기적 : 미국에
    # 23 / 삼국지 / 고사성어로 읽는 정사 삼국지
# driver.get(url_ip_check)
# driver.get(url_k_product)



def yes24_v3(keyword, page, n, title):
    print(yes24_v3)
    print(keyword)
    print("page:"+str(page) + " / n:"+str(n))

    n=n+1

    driver.get('http://www.yes24.com/')

    fakeKeywords = open('keyword.txt', 'r',  encoding='UTF8').read().split('\n')
    Keyword_3 = random.choices(fakeKeywords, k=3)

    for fKeyword in Keyword_3:
        # 책 제목 입력
        # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
        search_box = driver.find_element(By.CLASS_NAME, 'iptTxt')
        search_box.click()
        search_box.send_keys(fKeyword)
        delay()
        print(fKeyword)

        # 검색 버튼 클릭
        # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
        btn = driver.find_element(By.CLASS_NAME, 'schBtn')
        btn.click()
        delay_10()

        # document.getElementsByClassName('yesUI_pagen')[1].children[4].click()
        # document.getElementsByClassName('gd_name')[10].text
        targets = driver.find_elements(By.CLASS_NAME, 'lnk_img')
        # targets[10].click()
        targets[1].click()
        delay_n(20)

        # targets = driver.find_elements(By.CLASS_NAME, 'btnC m_size btn_blue')
        # targets[0].click()
        targets = driver.find_element(By.ID, 'addToCartForDetail')
        targets.click()
        delay_n(3)

        # targets = driver.find_elements(By.CLASS_NAME, 'bgYUI btn_popClose')
        targets = driver.find_elements(By.CLASS_NAME, 'popYUI_close')
        targets[4].click()
        delay_n(3)

        driver.back()
        delay_n(3)
        driver.back()
        delay_n(3)

    search_box = driver.find_element(By.CLASS_NAME, 'iptTxt')
    search_box.click()
    search_box.send_keys(keyword)
    delay()

    # 검색 버튼 클릭
    # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
    btn = driver.find_element(By.CLASS_NAME, 'schBtn')
    btn.click()
    delay_10()

    # document.getElementsByClassName('yesUI_pagen')[1].children[4].click()
    # document.getElementsByClassName('gd_name')[10].text
    page_elements = driver.find_elements(By.CLASS_NAME, 'gd_name')

    target = getTargetElement(page_elements, title)
    if target == 'empty':
        return;
    target.click()

    # 목적물 클릭
    # document.getElementsByClassName('bgYUI ico_nWin')[15].click()
    # targets = driver.find_element(By.CLASS_NAME, 'bgYUI ico_nWin')
    # targets = driver.find_elements(By.CLASS_NAME, 'lnk_img')
    # targets[10].click()
    # targets[22+n].click()
    delay_n(60)
    print(driver.current_url)
    print('clicked title : ' + driver.title)
    # 10 / 영어회화 / # 잡지] EBS 라디오 EASY ENGLISH 초급영어회화 (월간) : 12월 [2022] EBS 라디오 EASY ENGLISH 초급영어회화 (월간) : 12월 [2022] 새창이동
    # 23 / 영어회화 / 해커스톡 영어회화 10분의 기적 : 미국에
    # 23 / 삼국지 / 고사성어로 읽는 정사 삼국지
# driver.get(url_ip_check)
# driver.get(url_k_product)


def ypbook(keyword, page, n, title):
    print(keyword)
    print("page : " + str(page))
    # print(n)
    driver.get(url_ypbook)
    # 책 제목 입력
    # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
    search_box = driver.find_element(By.ID, 't_query')
    search_box.click()
    search_box.send_keys(keyword)
    # search_box.send_keys('삼국지')
    delay()

    # 검색 버튼 클릭
    # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
    btn = driver.find_element(By.CLASS_NAME, 'cm_sr')
    btn.click()
    delay_10()

    # 검색 아이템 늘리기
    target = driver.find_element(By.XPATH, '//*[@id="allFrame"]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/div/div[2]/div[3]/div')
    target.click()
    delay_n(3)
    target2 = driver.find_element(By.XPATH, '//*[@id="allFrame"]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/div/div[2]/div[3]/ul/li[4]')
    target2.click()

    # 타겟 아이템 클릭
    endFlag = False
    for i in range(1, 30):
        for j in range(1,4):
            t = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[' + str(i*2) + ']/div[2]/dl/dl[1]/dt/a['+str(j)+']')
            if t.text != '소득공제' and t.text != '베스트셀러' and t.text != 'YP 추천':
                if t.text == title:
                    print(t.text)
                    t.click()
                    endFlag = True
                    break
                else:
                    break
        if endFlag == True:
            break

    delay_n(30)

def aladin(keyword, page, n, title):
    print(keyword)
    print("page : " + str(page))
    print(n)

    page = page-2
    n = n-1

    driver.get(url_aladin)
    # 책 제목 입력
    # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
    search_box = driver.find_element(By.ID, 'SearchWord')
    search_box.click()
    search_box.send_keys(keyword)
    # search_box.send_keys('삼국지')
    delay()

    # 검색 버튼 클릭
    # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
    btn = driver.find_element(By.CLASS_NAME, 'searchBtn')
    btn.click()
    delay_10()

    # 페이지 이동
    # document.getElementsByClassName('bgYUI ico_nWin')[15].click()
    # targets = driver.find_element(By.CLASS_NAME, 'bgYUI ico_nWin')
    targets = driver.find_elements(By.CLASS_NAME, 'numoff')
    # targets[10].click()
    targets[page].click()
    delay_10()

    # 물건 클릭
    # document.getElementsByClassName('bgYUI ico_nWin')[15].click()
    elements = driver.find_elements(By.CLASS_NAME, 'bo3')
    target = getTargetElement(elements, title)
    if target == 'empty':
        return;
    target.click()

# '//*[@id="Search3_Result"]/div[11]/table/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/div[1]/ul/li[2]/a[1]/b'
# '/html/body/div[3]/table/tbody/tr/td[3]/form/div[2]/div[11]/table/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/div[1]/ul/li[2]/a[1]/b'
    print(targets)
    print(driver.current_url)
    print(driver.title)
    delay_10()
    # 10 / 영어회화 / 비즈니스 영어회화 표현사전 - 말로 하는 비즈니스에 다 통하는


def kyobo(keyword, page, n, title):
    print(keyword)
    print("page : " + str(page))
    print(n)
    page = page-1
    n = n-1
    driver.get(url_k_product)
    print('start kyobo')
    # // 돋보기 눌려서 product.kyobobook.co.kr로 진입
    # btn = driver.find_element(By.CLASS_NAME, 'btn_gnb_search')
    # btn.click()
    #
    # # btn_header_search
    # btn = driver.find_element(By.CLASS_NAME, 'btn_header_search')
    # btn.click()
    #
    # # // 검색하기 전 단계로 진입하기
    # search_box = driver.find_element(By.CLASS_NAME, 'btn_header_search')

    # search_box = driver.find_element(By.CLASS_NAME, 'ip_gnb_search')
    # search_box.send_keys('사국지')
    delay()
    # 검색창 클릭
    search_box = driver.find_element(By.ID, 'searchKeyword')
    search_box.click()
    delay()
    search_box.send_keys(keyword)
    delay()

    btn = driver.find_element(By.CLASS_NAME, 'btn_gnb_search')
    btn.click()
    delay()

    # 페이지 이동
    # document.getElementsByClassName('btn_page_num')[5]

    btn = driver.find_elements(By.CLASS_NAME, 'btn_page_num')
    btn[page].click()
    # delay()

    # 물건 클릭
    elements = driver.find_elements(By.CLASS_NAME,'prod_info')
    target = getTargetElement(elements, title)
    if target == 'empty':
        return;
    target.click()

    driver.implicitly_wait(20)
    # targetProduct = driver.find_element(By.CLASS_NAME, 'prod_info')
    # targetProduct = driver.find_elements(By.CLASS_NAME, 'prod_link')
    # targetProduct[n].click()
    # driver.find_element_by_xpath('//*[@class="prod_link"]').send_keys(Keys.ENTER)
    # targetProduct.click()
    # targetProduct.send_keys(Keys.ENTER)
    print(driver.title)
    print(driver.current_url)
    delay_n(60)

def getTargetElement(elements, title):
    idx = 0
    for e in elements:
        idx = idx +1
        t = e.text.find(title)
        if e.text.find(title) != -1:
            print('book idx : '+str(idx))
            return e
        # if e.text==title:
        #     return e
    # document.getElementsByClassName('prod_info')[0].children[2].textContent

    return 'empty'

#
# def getTargetElement(page_elements, title):
#     for e in page_elements:
#         if e.text == title:
#             return e;
#     return 'empty'

# [aladin, '중국어회화', 5, 1],



os.system('chcp 65001')
os.system('dir/w')



testList = [
            # [yes24_v3, '일본', 1, -4],
          #  [yes24_v3, '프랑스', 1, -3],
         #   [yes24_v3, '유럽', 1, -4],
          #  [aladin, '요리', 7, 5],
         #   [aladin, '유럽여행', 8, 7],
            [kyobo, '유럽여행', 5, 8],
            [kyobo, '영어회화', 6, 2],
            ]

testList_1214 = [
            # [yes24_v3, '일본', 1, -4],
            # [yes24_v3, '프랑스', 1, -12],
            [yes24_v3, '유럽', 1, -2],
            [aladin, '요리', 7, 16],
            [aladin, '유럽여행', 8, 7],
            [kyobo, '유럽여행', 5, 7],
            [kyobo, '영어회화', 6, 8],
            ]


testList_1215 = [
                # [yes24_v3, '프랑스', 1, -2, '해시태그 프랑스 한 달 살기'],
            #    [yes24_v3, '유럽', 1, -2, '마음까지 따듯해지는 북유럽 스타일 손뜨개 소품'],
                [aladin, '요리', 7, -2, 'Why? 역사 속 음식과 요리'],
                [aladin, '유럽여행', 8, -2, '북유럽 셀프 트래블'],
                [kyobo, '유럽여행', 5, -2, '[국내도서] 현지에서 바로 쓰는 유럽 5개국 여행회화'],
                [kyobo, '영어회화', 6, -2, '[국내도서] 야나두 영어회화'],
                # [ypbook, '삼국지', 6, -2, '[국내도서] 야나두 영어회화'],
]

testList_1215 = [
                [yes24_v3, '프랑스', 1, -2, '해시태그 프랑스 한 달 살기'],
               [yes24_v3, '유럽', 1, -2, '마음까지 따듯해지는 북유럽 스타일 손뜨개 소품'],
               [aladin, '요리', 7, -2, 'Why? 역사 속 음식과 요리'],
               [aladin, '유럽여행', 8, -2, '북유럽 셀프 트래블'],
                [kyobo, '유럽여행', 3, -2, '[국내도서] 현지에서 바로 쓰는 유럽 5개국 여행회화'],
                [kyobo, '영어회화', 4, -2, '[국내도서] 야나두 영어회화'],
                # [ypbook, '삼국지', 6, -2, '[국내도서] 야나두 영어회화'],
]

testList_1217 = [
            [yes24_v3, '프랑스', 1, -2, '해시태그 프랑스 한 달 살기'],
            [yes24_v3, '유럽', 1, -2, '마음까지 따듯해지는 북유럽 스타일 손뜨개 소품'],
            [aladin, '요리', 7, -2, 'Why? 역사 속 음식과 요리'],
            [aladin, '유럽여행', 8, -2, '북유럽 셀프 트래블'],
            [kyobo, '유럽여행', 3, -2, '[국내도서] 현지에서 바로 쓰는 유럽 5개국 여행회화'],
            [kyobo, '영어회화', 5, -2, '[국내도서] 야나두 영어회화'],
            [ypbook, '영어회화', 3, -2, '영어회화공식 231+54 : 기본'],
]
# main
s = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
logging.basicConfig(filename='C:/Users/c.won/Documents/카카오톡 받은 파일/pythonProject/pythonProject/qwqwqw.txt', encoding='utf-8', level=logging.DEBUG)
logging.debug('startTime : ' + s)
print('startTime : ' + s)
# driver = getTorDriver()
for do in testList_1217:
    for i in range(1, 70):
        driver = open_browser_c()
        try:
            # print('step1 ip check')
            # driver.get(url_ip_check)
            # driver.delete_all_cookies()
            print('step2 ip check')
            keyword = do[1]
            page = do[2]
            n = do[3]
            title = do[4]
            print('cycle : '+str(i))
            print(driver.title)
            print(driver.current_url)
            do[0](keyword, page, n, title)
            driver.quit()
            print('------------------------------')

        except Exception as e:
            print("exception!!! : ",e)
            driver.quit()
        # yes24()
        # aladin()
