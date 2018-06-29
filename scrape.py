from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

Catalog = {}

driver = webdriver.Chrome()
driver.get("https://catalog.uncc.edu/preview_program.php?catoid=23&poid=5578")
soup = BeautifulSoup(driver.page_source, 'lxml')
Catalog["name"] = str(soup.find(id="acalog-page-title").string).strip()

print(Catalog["name"])

driver.close()
