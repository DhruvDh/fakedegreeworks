from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from finders import *

driver = webdriver.Chrome()
driver.get("https://catalog.uncc.edu/preview_program.php?catoid=23&poid=5567")

Program = {}

Program["name"] = find(driver, name).text.strip()
Program['desc'] = get_text(driver, desc)


print("Name: " + Program["name"])
print("---------------------------------------------------------")
print("Desc: " + Program["desc"])
print("---------------------------------------------------------")
print("Admission: " + Program["admis_req"])
print("---------------------------------------------------------")
print("Degree: " + Program["deg_req"])
print("---------------------------------------------------------")

driver.close()
