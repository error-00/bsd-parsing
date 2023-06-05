import time

import requests
from bs4 import BeautifulSoup
import re

from seleniumwire import webdriver

from load_django import *
from app_parser.models import *

headers = {"User-Agent": "Mozilla/5.0"}


def get_proxies():
    username = 'france_user3'
    password = 'dfs345sdfEADS33'
    entry = ('http://customer-%s:%s@dc.gb-pr.oxylabs.io:46000' %
             (username, password))
    proxies = {
        "http": entry,
        "https": entry,
    }

    return proxies


seleniumwire_options = {
    'proxy': get_proxies(),
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options, options=chrome_options)
# driver = webdriver.Chrome(options=chrome_options)


for l in Link.objects.filter(status='New'):
    url = l.link

    print()
    print('################################')
    print(url)

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(5)

    name = l.name
    print('Name: ', name)

    try:
        type = soup.find('span', attrs={
            'id': 'ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBEDetail_lBETypeValue'}).text.strip()
    except AttributeError:
        type = None
    print('Type: ', type)

    try:
        domesticity = soup.find('span', attrs={
            'id': 'ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBEDetail_lDomesticityValue'}).text.strip()
    except AttributeError:
        domesticity = None
    print('Domesticity: ', domesticity)

    try:
        registered_agent = soup.find('span', attrs={
            'id': 'ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBEDetail_lRegAgentValue'}).text.strip()
    except AttributeError:
        registered_agent = None
    print('Registered Agent: ', registered_agent)

    try:
        date_formed = soup.find('span', attrs={
            'id': 'ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBEDetail_lCreatedValue'}).text.strip()
    except AttributeError:
        date_formed = None
    print('Date Formed: ', date_formed)

    try:
        duration = soup.find('span', attrs={
            'id': 'ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBEDetail_lDurationValue'}).text.strip()
    except AttributeError:
        duration = None
    print('Duration: ', duration)

    try:
        renewal_month = soup.find('span', attrs={
            'id': 'ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBEDetail_lFiscalMonthValue'}).text.strip()
    except AttributeError:
        renewal_month = None
    print('Renewal Month: ', renewal_month)

    try:
        report_due = soup.find('span', attrs={
            'id': 'ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBEDetail_lARDueValue'}).text.strip()
    except AttributeError:
        report_due = None
    print('Report Due: ', report_due)

    try:
        chapter = soup.find('span', attrs={
            'id': 'ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBEDetail_lBEBINValue'}).text.strip()
    except AttributeError:
        chapter = None
    print('Charter No.: ', chapter)

    try:
        home_state = soup.find('span', attrs={
            'id': 'ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBEDetail_lStateCountryValue'}).text.strip()
    except AttributeError:
        home_state = None
    print('Home State: ', home_state)

    try:
        status = soup.find('span', attrs={
            'id': 'ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBEDetail_lStatusValue'}).text.strip()
    except AttributeError:
        status = None
    print('Status: ', status)

    defaults = {
        'name': name,
        'type': type,
        'domesticity': domesticity,
        'registered_agent': registered_agent,
        'date_formed': date_formed,
        'duration': duration,
        'renewal_month': renewal_month,
        'report_due': report_due,
        'chapter': chapter,
        'home_state': home_state,
        'status': status,
    }

    l.status = 'Done'
    l.save()

    obj, created = Info.objects.get_or_create(
        link=url,
        defaults=defaults,
    )

    time.sleep(5)

driver.quit()
