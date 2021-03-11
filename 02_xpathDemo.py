from selenium import webdriver
import time

driver = webdriver.Firefox()
time.sleep(3)
driver.get("http://www.baidu.com")
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='kw']").send_keys('hello')
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='su']").click()
time.sleep(3)
print("自动化完毕")
driver.quit()
