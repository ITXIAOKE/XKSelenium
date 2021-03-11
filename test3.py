from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(2)
driver.find_element_by_link_text("登录").click()
time.sleep(2)
driver.find_element_by_link_text("立即注册").click()
time.sleep(4)
driver.quit()

from lettuce import release
