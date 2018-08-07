from selene.api import *
import elle
from selenium import webdriver
from selene import browser
import sys, time
import ssl
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

elle.driver_config('android')

#browser.open_url("https://admin.elle.ru")

elle.auth_elle('dev','dev')

elle.env('.v.x')

elle.auth_elle('epoluyan','asd@3124lun1')
elle.assert_enter()

elle.auth_elle('213adasd','Epoluyan1')
elle.assert_enter()

elle.auth_elle('epoluyan','Epoluyan1')

if(browser.title() == "Админка ELLE.RU"):

    print ("Success: Заголовок правильный")

else:

    assert print ("Failed: Заголовок не корректный")

elle.articles_add()

elle.main_page()

elle.articles()

elle.fashion_shows()

elle.prerolls()

elle.users()

elle.uploader()

elle.exit_logging()

