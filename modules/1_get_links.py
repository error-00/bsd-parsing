import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from load_django import *
from app_parser.models import *

headers = {"User-Agent": "Mozilla/5.0"}

urls_list = [
    'https://bsd.sos.mo.gov/BusinessEntity/BESearch.aspx?SearchType=0',
]

driver = webdriver.Chrome()

for url in urls_list:
    for key in Keys_w.objects.filter(status='New'):
        key_word = key.name
        driver.get(url)

        driver.find_element(By.XPATH, "//input[@class='swRequiredTextbox form-control']").send_keys(key_word)
        driver.find_element(By.XPATH,
                            "//a[@id='ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBESearch_bsPanel_stdbtnSearch_LinkStandardButton']").send_keys(
            Keys.ENTER)

        end = driver.find_element(By.XPATH, "//div[@class='rgWrap rgInfoPart']/strong[2]").text.strip()

        while True:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            business_list = soup.find_all('tr', attrs={
                'class': 'rgRow'})

            for product in business_list:
                print()
                business_name = product.find_all('td')[2].text.strip()
                print(business_name)

                link = product.find('a')['href']
                if link.startswith('http'):
                    pass

                else:
                    business_link = 'https://bsd.sos.mo.gov' + link
                    print(business_link)

                    defaults = {
                        'name': business_name,
                    }

                    obj, created = Link.objects.get_or_create(
                        link=business_link,
                        defaults=defaults,
                    )

            if driver.find_element(By.XPATH, "//div[@class='rgWrap rgInfoPart']/strong[1]").get_attribute('innerHTML') == end:
                key.status = 'Done'
                key.save()
                break
            else:
                driver.find_element(By.XPATH, "//input[@class='rgPageNext']").click()

driver.quit()

