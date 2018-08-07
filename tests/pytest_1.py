from selene.api import *
from selenium import webdriver
from selene import browser
from selene.browser import open_url
from selene.support.jquery_style_selectors import s, ss
from selene.support.conditions import have
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#config.browser_name  = "chrome"

desired_cap = {
 'browser': 'Safari',
 'browser_version': '11.0',
 'os': 'OS X',
 'os_version': 'High Sierra',
 'resolution': '1024x768'
}

desired_cap['acceptSslCerts'] = True

driver = webdriver.Remote(
    command_executor='http://sergeyparfenov1:MY7SQ93bmVn2ozxrhRws@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)


browser.set_driver(driver)

browser.open_url("https://www.maximonline.ru.e.x/")

login_button = s("#header > div.header__line.header__line_one > div.login-block_redesign > div > a.login-block-login.pop").click()

login_form = s("#regauth_login").set("5ytzu@2odem.com")

driver.save_screenshot('screen.png')

pass_form = s("#regauth_pass").set("123456")

button_submit = s(".standard-button-newdesign").click()

print (driver.title)

print ('тест выполнен')







