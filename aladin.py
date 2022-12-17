import inspect, os, platform, time, random, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class ALADIN_LOGIC:
    url_aladin = 'https://www.aladin.co.kr/'
    def __init__(self, driver):
        self.driver = driver
        self.proxy = self.proxy_create()
        self.crawling()

    def aladin_v1(self):
        self.driver.get(self.url_aladin)
        # 책 제목 입력
        # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
        search_box = self.driver.find_element(By.ID, 'SearchWord')
        search_box.click()
        search_box.send_keys('영어회화')
        # search_box.send_keys('삼국지')
        self.delay()

        # 검색 버튼 클릭
        # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
        btn = self.driver.find_element(By.CLASS_NAME, 'searchBtn')
        btn.click()
        self.delay_10()

        # 페이지 이동
        # document.getElementsByClassName('bgYUI ico_nWin')[15].click()
        # targets = driver.find_element(By.CLASS_NAME, 'bgYUI ico_nWin')
        targets = self.driver.find_elements(By.CLASS_NAME, 'numoff')
        # targets[10].click()
        targets[7].click()
        self.delay_10()

        # 물건 클릭
        # document.getElementsByClassName('bgYUI ico_nWin')[15].click()
        targets = self.driver.find_elements(By.CLASS_NAME, 'bo3')
        # targets = driver.find_elements(By.CLASS_NAME, 'front_cover i_cover')
        # targets[10].click()
        targets[3].click()
        print(targets)
        self.delay_10()
        # 10 / 영어회화 / 비즈니스 영어회화 표현사전 - 말로 하는 비즈니스에 다 통하는

    def __delay(self):
        wait_time = random.uniform(5, 10)
        self.driver.implicitly_wait(wait_time)

    def __delay_10(self):
        wait_time = random.uniform(10, 20)
        self.driver.implicitly_wait(wait_time)
