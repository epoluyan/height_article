from selene.api import *
from selenium import webdriver

def driver_config(value):

    if (value == "chrome"):

        config.browser_name = "chrome"

        browser.open_url("https://www.admin.elle.ru/")

    elif (value == "safari"):

        desired_cap = {
            'browser': 'Safari',
            'browser_version': '11.0',
            'os': 'OS X',
            'os_version': 'High Sierra',
            'resolution': '1900x768',
            'browserstack.local': 'true',
            'acceptSslCerts': 'true',
            'acceptSslCert': 'true',
            'browserstack.localIdentifier': 'Test123'

        }

        driver = webdriver.Remote(
            command_executor='http://sergeyparfenov1:MY7SQ93bmVn2ozxrhRws@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)

        browser.set_driver(driver)

        browser.open_url("https://www.admin.elle.ru/")

    elif (value == "ios"):

        desired_cap = {

            'browserName': 'iPhone',
            'device': 'iPhone 7',
            'realMobile': 'true',
            'os_version': '10.3',
            'browserstack.local': 'true',
            'acceptSslCerts': 'true',
            'acceptSslCert': 'true',
            'browserstack.localIdentifier': 'Test123'

        }

        driver = webdriver.Remote(
            command_executor='http://sergeyparfenov1:MY7SQ93bmVn2ozxrhRws@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)

        browser.set_driver(driver)

        browser.open_url("https://www.admin.elle.ru/")

    elif (value == "android"):

        desired_cap = {
            'browserName': 'android',
            'device': 'Samsung Galaxy S8',
            'realMobile': 'true',
            'os_version': '7.0',
            'browserstack.local': 'true',
            'acceptSslCerts': 'true',
            'acceptSslCert': 'true',
            'browserstack.localIdentifier': 'Test123'
        }

        driver = webdriver.Remote(
            command_executor='http://sergeyparfenov1:MY7SQ93bmVn2ozxrhRws@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)

        browser.set_driver(driver)

        browser.open_url("https://www.admin.elle.ru/")


def env(x):

    s("#__BVID__12").set(x)

def auth_elle(name, password):

    s("#__BVID__9").set(name)
    s("#__BVID__10").set(password)
    s("body > div.background.d-flex.justify-content-center > div > form > div > div > button > svg").click()

def assert_enter():

    s('body > div.background.d-flex.justify-content-center > div > div').should(be.visible)
    s("body > div.background.d-flex.justify-content-center > div > div").should(have.exact_text('Неверный логин или пароль'))

#Разделы админки

def articles_add():

    s("#app > div.app-side-menu > nav > div.side-menu__content > ul > li:nth-child(1) > a > div.menu-item__icon > svg > path").click()
    s('#app > div.app-content > div > div.articles-editor__page > textarea.borderless-input.article-title').should(be.visible)
    s("#app > div.app-content > div > div.articles-editor__toolbar > div > button.btn.btn-success.button-save > span").should(have.exact_text('Сохранить'))

def main_page():

    s("#app > div.app-side-menu > nav > div.side-menu__content > ul > li:nth-child(2) > a > div.menu-item__icon > svg").click()
    s('#app > div.app-content > div > div.dashboard__bottom > div > div:nth-child(1) > div > h6 > span').should(be.visible)
    s("#app > div.app-content > div > div.dashboard__bottom > div > div:nth-child(2) > div > h6 > span").should(have.exact_text('Эффективность статей за'))

def articles():

    s("#app > div.app-side-menu > nav > div.side-menu__content > ul > li:nth-child(3) > a > div.menu-item__icon > svg").click()
    s('#app > div.app-content > div > div:nth-child(3) > div:nth-child(1) > h5').should(be.visible)
    s("#app > div.app-content > div > h1").should(have.exact_text('Статьи'))

def fashion_shows():

    s("#app > div.app-side-menu > nav > div.side-menu__content > ul > li:nth-child(4) > a > div.menu-item__icon > svg").click()
    s('#app > div.app-content > div > div:nth-child(3) > div > h5').should(be.visible)
    s("#app > div.app-content > div > h1 > span").should(have.exact_text('Показы'))

def prerolls():

    s("#app > div.app-side-menu > nav > div.side-menu__content > ul > li:nth-child(5) > a > div.menu-item__icon > svg").click()
    s('#app > div.app-content > div > div:nth-child(3) > div > h5').should(be.visible)
    s("#app > div.app-content > div > h1 > span").should(have.exact_text('Прероллы'))

def users():

    s("#app > div.app-side-menu > nav > div.side-menu__content > ul > li:nth-child(6) > a > div.menu-item__icon > svg > path").click()
    s('#__BVID__43 > thead > tr > th:nth-child(1)').should(be.visible)
    s("#app > div.app-content > div > h1 > a").should(have.exact_text('Создать пользователя'))

def uploader():

    s("#app > div.app-side-menu > nav > div.side-menu__content > ul > li:nth-child(7) > a > div.menu-item__icon > svg").click()
    s('#app > div.app-content > div > div > div > div > div.upload-zone__text').should(be.visible)
    s("#app > div.app-content > div > h1").should(have.exact_text('Загрузка файлов'))

def exit_logging():

    s("#app > div.app-side-menu > nav > div.side-menu__bottom > ul > li:nth-child(1) > button > div.menu-item__icon > svg > path").click()
    s('body > div.background.d-flex.justify-content-center > div > form').should(be.visible)