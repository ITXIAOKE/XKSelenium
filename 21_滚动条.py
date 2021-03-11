from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

js = "var a=document.documentElement.scrollTop=100000"
driver.execute_script(js)
sleep(2)

js = "var a=document.documentElement.scrollTop=0"
driver.execute_script(js)
sleep(2)

driver.quit()
