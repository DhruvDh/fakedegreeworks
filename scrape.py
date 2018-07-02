from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from finders import *
from lib import *

driver = webdriver.Chrome()
driver.get("https://catalog.uncc.edu/preview_program.php?catoid=23&poid=5567")

cs = Program()

cs.name = find(driver, name).text.strip()
cs.desc = get_text(driver, desc)


print("Name: " + cs.name)
print("---------------------------------------------------------")
print("Desc: " + cs.desc)
print("---------------------------------------------------------")

driver.close()
