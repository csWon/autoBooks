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


url_ip_check = 'https://ko.infobyip.com/'
url_k_product = 'https://product.kyobobook.co.kr/'
url_naver = 'https://www.naver.com'

# with Controller.from_port(port=9051) as controller:
#     while True:
#         url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%B4%EC%95%84%EC%9D%B4%ED%94%BC"
#         hostname = "socks5://127.0.0.1"
#         port = "9050"
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--proxy-server=%s' % hostname + ":" + port)
#         driver = webdriver.Chrome(options=chrome_options)
#
#         driver.get(url)
#         time.sleep(20)
#         driver.quit()
#
#         controller.authenticate('')
#         controller.signal(Signal.NEWNYM)
#
#         if controller.is_newnym_available() == False:
#             print("waiting for Tor to change IP: " + str(controller.get_newnym_wait()) + " sec")
#             time.sleep(controller.get_newnym_wait())
#
# controller.close()

def delay():
    wait_time = random.uniform(1, 3)
    driver.implicitly_wait(wait_time)

def open_browser_c():
    chrome_path = '/usr/local/bin/chromedriver'
    torexe = os.popen(r'/usr/local/bin/tor')
    # torexe = os.popen(r'/opt/homebrew/opt/tor/bin/tor')
    # PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT
    # PROXY = "socks5://127.0.0.1:9150"  # IP:PORT or HOST:PORT

    prx = open('ip.txt', 'r').read().split('\n')

    # 프록시 랜덤 선택
    PROXY = random.choice(prx)

    chrome_options = webdriver.ChromeOptions()
    # options.add_argument('window-size=1920,1080')
    # 옵션 설정
    chrome_options = webdriver.ChromeOptions()
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
       # Tor 프록시 설정 (ip 우회)
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.headless = True

    # 선택된 아이피 프린트
    print(PROXY)

    # 아이피 적용
    # webdriver.DesiredCapabilities.CHROME['proxy'] = {
    #     "httpProxy": PROXY,
    #     "ftpProxy": PROXY,
    #     "sslProxy": PROXY,
    #     "proxyType": "MANUAL"
    # }
    # 브라우저 열기
    # driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    driver = webdriver.Chrome()

    return driver


for i in range(1, 11):
    driver = open_browser_c()
    driver.get(url_ip_check)
    driver.get(url_k_product)

    # driver.delete_all_cookies()
    delay()
    print(i)
    print(driver.title)
    print(driver.current_url)

    action = ActionChains(driver)

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

    # 검색창 클릭
    search_box = driver.find_element(By.ID, 'searchKeyword')
    search_box.click()
    search_box.send_keys('영어회화')
    delay()

    btn = driver.find_element(By.CLASS_NAME, 'btn_gnb_search')
    btn.click()
    delay()

    # 페이지 이동
    # document.getElementsByClassName('btn_page_num')[5]
    btn = driver.find_elements(By.CLASS_NAME, 'btn_page_num')
    btn[5].click()
    delay()

    # 물건 클릭
    driver.implicitly_wait(3)
    targetProduct = driver.find_element(By.CLASS_NAME, 'prod_info')
    targetProduct.click()
    print(driver.current_url)
    delay()





# # 이거 둘다 됨
# # document.getElementsByClassName('product_detail_area product_person')[0].getElementsByClassName('ico_wish')[0].click()
# # document.getElementsByClassName('btn_wish_alarm size_md')[0].click()
#
# personBox = driver.find_element(By.CLASS_NAME, 'product_detail_area.product_person')
# lg_wish_btn = driver.find_element(By.CLASS_NAME, 'btn_wish.size_lg')
# lg_wish_btn.click()
# driver.implicitly_wait(3)
#
# # input()
#
#
# loginPage_moveBtn = driver.find_elements(By.CLASS_NAME, 'btn_md.btn_primary')
# print(len(loginPage_moveBtn))
# print(loginPage_moveBtn[len(loginPage_moveBtn)-1])
# loginPage_moveBtn[len(loginPage_moveBtn)-1].click()
#
# # 교보문고 로그인 페이지
# naver_login_btn = driver.find_elements(By.CLASS_NAME, 'btn_sns_login.naver')
# naver_login_btn[0].click()







#
# # NAVER 로그인 페이지
# id = 'dobee0101'
# pw = 'wnehdckdtjq'
#
#
# idSlot = driver.find_element(By.ID, 'id')
# idSlot.click()
# pyperclip.copy(id)
# idSlot.send_keys(Keys.COMMAND, 'v')
# time.sleep(2)
#
# passwordSlot = driver.find_element(By.ID, 'pw')
# passwordSlot.click()
# pyperclip.copy(pw)
# passwordSlot.send_keys(Keys.COMMAND, 'v')
# time.sleep(2)
#
# naver_login_btn = driver.find_element(By.ID, 'log.login')
# naver_login_btn.click()
# input()
#
# input()
#
#
# # wnehdckdtjq
# input()
# print(loginPage_moveBtn.is_displayed())
# print(loginPage_moveBtn.is_enabled())
# print(loginPage_moveBtn.is_selected())
# # loginPage_moveBtn.click()
#
# input()
#
# # print(driver.page_source)
# driver.implicitly_wait(3)
# loginPage_moveBtn.send_keys(Keys.ENTER)
# input()
# loginPage_moveDialog = driver.find_element(By.CLASS_NAME, 'dialog_wrap.ui-dialog-content.ui-widget-content.initialized')
# loginPage_moveDialog.find_element()
#
# # driver.find_element(By.XPATH,)
#
#
# # sourcecode_elem = driver.find_element_by_xpath("//div[@class='language-text highlighter-rouge']/pre[@class='highlight']/code")
# loginPage_moveBtn = loginPage_moveDialog.find_elements(By.CLASS_NAME, 'kbb_loaded.dialog_open')
# print(loginPage_moveBtn)
# print("Element is visible? " + str(loginPage_moveBtn.is_displayed()))
# action.move_to_element(loginPage_moveBtn).perform()
# print("Element is visible? " + str(loginPage_moveBtn.is_displayed()))
#
# # loginPage_moveBtn.click()
# input()
# # <button class="btn_md btn_primary"><span class="text">확인</span></button>
#
#
# print("Element is visible? " + str(loginPage_moveBtn.is_displayed()))
# action.move_to_element(loginPage_moveBtn).perform()
# print("Element is visible? " + str(loginPage_moveBtn.is_displayed()))
# loginPage_moveBtn.click()
# # document.getElementsByClassName('btn_wish size_lg')[0].click()
#
# print(personBox)
# input()
# # person_wish_btn = product_person_area.find_element(By.CLASS_NAME, 'ico_wish')
# # person_wish_btn.click()
#
# input()
#
# checkBox = driver.find_element(By.ID, 'chkAllSeries')
# # checkBox = driver.find_element(By.CLASS_NAME, 'form_chk')
# action.move_to_element(checkBox).perform()
# # driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#
#
# input()
#
# checkBox.click()
#
#
# wishBtn = driver.find_element(By.CLASS_NAME, 'ico_wish')
# wishBtn.click()
#
# loginPage_moveBtn = driver.find_element(By.CLASS_NAME, 'btn_md.btn_primary')
# loginPage_moveBtn.click()
# input()
#
#
# driver.close()

#<button type="button" data-kbbfn="wish-item" data-kbbfn-myrcode="001" data-kbbfn-nbopcode="005" data-kbbfn-id="2001937901" class="btn_wish_alarm size_md"><span class="ico_wish"></span><span class="hidden">찜/알림 설정하기</span></button>
# <div class="dialog_wrap ui-dialog-content ui-widget-content initialized" data-class="dialog_alert" style="width: auto; min-height: 0px; max-height: none; height: auto;" id="ui-id-49"><div class="dialog_contents"><p class="alert_text">로그인 후 이용가능합니다</p><p class="alert_text_sm">로그인 페이지로 이동하시겠습니까?</p></div><div class="dialog_footer"><button class="btn_md btn_light_gray"><span class="text">취소</span></button><button class="btn_md btn_primary"><span class="text">확인</span></button></div></div>