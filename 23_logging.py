
from selenium import webdriver
import logging

logging.basicConfig(level=logging.DEBUG)
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

driver.quit()

