from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")
time.sleep(3)
driver.find_element_by_id("translateContent").send_keys("传智播客")
time.sleep(3)
driver.find_element_by_id("translateContent").submit()
time.sleep(6)

driver.quit()
