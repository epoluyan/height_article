from selene.api import *
import allure
from selene import config
from selene.driver import SeleneDriver
from selenium.webdriver import Firefox
from selene.support.conditions import have
from selenium import webdriver

browser = webdriver.Firefox()

#config.browser_name  = "chrome"

#driver = SeleneDriver.wrap(Firefox())
#browser.open_url("https://www.maximonline.ru/")

browser.get("https://www.maximonline.ru/")

login_button = s("#header > div.header__line.header__line_one > div.login-block_redesign > div > a.login-block-login.pop").click()

login_form = s("#regauth_login").set("5ytzu@2odem.com")

pass_form = s("#regauth_pass").set("123456")

button_submit = s(".standard-button-newdesign").click()








