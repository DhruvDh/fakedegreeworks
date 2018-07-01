from lib import *
from selenium import webdriver


def find(driver: webdriver, xpath: str) -> str:
    try:
        return driver.find_element_by_xpath(xpath)
    except:
        print("Couldn't find " + xpath)
        return None


def get_text(driver: webdriver, xpath: str) -> str:
    i = 1
    suffix = ''
    result = ""
    while find(driver, xpath + suffix) is not None:
        if result == "":
            result = find(driver, xpath + suffix).text.strip()
        else:
            result = result + "\n" + find(driver, xpath + suffix).text.strip()
        i = i + 1
        suffix = '[' + str(i) + ']'
    return None if result == "" else result
