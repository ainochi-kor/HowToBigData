import time
import pandas as pd
import math

from selenium import webdriver
from bs4 import BeautifulSoup
#from Selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('chromedriver_win32\chromedriver.exe')
driver.get('http://www.encar.com/pr/pr_index.do?WT.hit=index_gnb')
time.sleep(1.5)
#팝업창 닫기
driver.find_element_by_css_selector('#depth_main > div.layer_mdl.layer_guide.ui_guide.on > div.layer_container.ui_start > a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#csv파일로 만들 배열 생성
user_car_info = []
for comp_index in range(2,71):
    #메뉴선택
    driver.find_element_by_xpath('//*[@id="depth_main"]/div[2]/div/div[1]/div[1]/div[2]/ul/li[1]/div/a').click()
    driver.find_element_by_xpath('//*[@id="depth_main"]/div[2]/div/div[1]/div[1]/div[2]/ul/li[1]/div/div/div[1]/ul/li['+str(comp_index)+']/a').click()
    #로딩을 기다리는 시간
    time.sleep(1.5)
    #page의 갯수를 구하기 위해 검색결과를 뽑아옴.
    page_num = soup.select('#resultWrap > div.ui_tab_container > div.result_buy.ui_tab_content.on > div.buy_title > span')
    #검색결과 출력
    print(page_num)
    #검색결과를 str로 변경
    page_num = str(page_num)
    #숫자만 뽑아서int형으로 바꾸기.
    page_num = int(page_num[24:-9].replace(",",""))
    page = math.trunc(page_num/5)

    print(page_num)
    print(page)

    for i in range(1,page):
        if i > 10 and (i%10)-1 == 0:
            print("test")
            next10 = driver.find_element_by_css_selector('#resultWrap > div.ui_tab_container > div.result_buy.ui_tab_content.on > div.part.page > span.next > a')
            driver.execute_script("arguments[0].click();", next10)
            time.sleep(1.5)
        company = soup.select(
            '#resultWrap > div.ui_tab_container > div.result_buy.ui_tab_content.on > table > tbody > tr > td > a > span.inf > span.cls > strong'
        )
        model = soup.select(
            '#resultWrap > div.ui_tab_container > div.result_buy.ui_tab_content.on > table > tbody > tr > td > a > span.inf > span.cls > em'
        )
        engine = soup.select(
            '#resultWrap > div.ui_tab_container > div.result_buy.ui_tab_content.on > table > tbody > tr > td > a > span.inf > span.dtl > strong'
        )

        engine2 = soup.select(
            '#resultWrap > div.ui_tab_container > div.result_buy.ui_tab_content.on > table > tbody > tr > td > a > span.inf > span.dtl > em'
        )

        year = soup.select(
            '#resultWrap > div.ui_tab_container > div.result_buy.ui_tab_content.on > table > tbody > tr > td > a > span.detail > span.yer'
        )

        km = soup.select(
            '#resultWrap > div.ui_tab_container > div.result_buy.ui_tab_content.on > table > tbody > tr > td > a > span.detail > span.km'
        )

        location = soup.select(
            '#resultWrap > div.ui_tab_container > div.result_buy.ui_tab_content.on > table > tbody > tr > td > a > span.detail > span.lo'
        )

        money = soup.select(
            '#resultWrap > div.ui_tab_container > div.result_buy.ui_tab_content.on > table > tbody > tr > td > a > span.val > span > strong'
        )

        for item in zip(company, model, engine, engine2, year, km, location, money):
            user_car_info.append(
                {
                    'company': item[0].text,
                    'model': item[1].text,
                    'engine': item[2].text,
                    'engine2': item[3].text,
                    'year': item[4].text,
                    'km': item[5].text,
                    'location': item[6].text,
                    'money': item[7].text,
                }
            )
        print(i)
        driver.find_element_by_link_text(str(i))


data = pd.DataFrame(user_car_info)
print(data)
data.to_csv('encar_used_car_hyundai_info.csv')
#driver.close()
#driver.quit()