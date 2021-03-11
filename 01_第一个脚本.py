from selenium import webdriver
import time
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
time.sleep(3)
driver.get("http://www.baidu.com")
time.sleep(3)
driver.find_element_by_id('kw').send_keys('selenium3')
time.sleep(3)
driver.find_element_by_id('su').click()
time.sleep(3)

driver.close()
