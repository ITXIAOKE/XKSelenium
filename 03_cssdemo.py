from selenium import webdriver
import time
driver = webdriver.Firefox()
time.sleep(2)
driver.get("http://www.baidu.com")
time.sleep(2)
driver.find_element_by_css_selector("#kw").send_keys("传智播客")
time.sleep(2)
driver.find_element_by_css_selector("#su").click()
time.sleep(2)
driver.quit()
