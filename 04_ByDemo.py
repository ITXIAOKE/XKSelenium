from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
import time
time.sleep(4)
driver.find_element(By.XPATH, ".//*[@class='s_ipt']").send_keys("传智播客")
driver.find_element(By.ID, "su").click()
driver.quit()
