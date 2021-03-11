from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
import time

time.sleep(5)
# 设置窗口的大小
# driver.set_window_size(480, 800)
# 窗口最大化
driver.maximize_window()
time.sleep(5)

driver.quit()
