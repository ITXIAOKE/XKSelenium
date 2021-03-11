from selenium import webdriver
import time

# time.sleep(2)
url = "http://www.baidu.com"
driver = webdriver.Firefox()
# time.sleep(2)
driver.get(url)

second_url = "http://map.baidu.com/"
time.sleep(2)
driver.get(second_url)
time.sleep(2)
# 浏览器返回到前一个页面
driver.back()
time.sleep(4)
# 浏览器回退到之前的页面
driver.forward()
time.sleep(4)

driver.quit()
