from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://catalog.uncc.edu/preview_program.php?catoid=23&poid=5578")
assert "Program" in driver.title
driver.close()