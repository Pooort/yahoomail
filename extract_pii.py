import argparse

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from helpers import get_web_driver


def print_info(login, password):

    webdriver = get_web_driver(headless=True)

    webdriver.get('https://mail.yahoo.com')
    webdriver.find_element_by_xpath('//a[@class="fuji-button-link fuji-button-text fuji-button-inverted"]').click()
    element = WebDriverWait(webdriver, 10).until(
        EC.presence_of_element_located((By.ID, "login-username"))
    )
    element.send_keys(login)
    webdriver.find_element_by_id("login-signin").submit()
    element = WebDriverWait(webdriver, 10).until(
        EC.presence_of_element_located((By.ID, "login-passwd"))
    )
    element.send_keys(password)
    element.send_keys(Keys.ENTER)
    webdriver.find_element_by_xpath('//label[@role="presentation"]').click()
    webdriver.find_element_by_css_selector('#ybarAccountMenuBody > ul > li > div > a').click()
    opened_tab = webdriver.window_handles[-1]
    webdriver.switch_to.window(opened_tab)
    firstname = webdriver.find_element_by_id('txt-first-name').text
    lastname = webdriver.find_element_by_id('txt-last-name').text
    gender = webdriver.find_element_by_id('txt-gender').text
    birthdate = webdriver.find_element_by_xpath('//li[@id="birthday"]/div[@class="txt"]').text
    print('firstname: {}'.format(firstname))
    print('lastname: {}'.format(lastname))
    print('phone: None')
    print('birthdate: {}'.format(birthdate))
    print('address: None')
    print('country: None')
    print('city: None')
    print('zip: None')
    print('gender: {}'.format(gender))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract personal information from yahoo email account.')
    parser.add_argument('--login')
    parser.add_argument('--password')
    args = parser.parse_args()
    print_info(args.login, args.password)
