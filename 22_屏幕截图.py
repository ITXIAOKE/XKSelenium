from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
# driver.implicitly_wait(1)
# driver.maximize_window()
driver.get("http://www.baidu.com")
sleep(2)
try:
    driver.find_element_by_id("kw_error").send_keys("selenium")
    driver.find_element_by_id("su").click()
    sleep(2)
except:
    driver.get_screenshot_as_file("D:\\baidu.jpg")
    sleep(2)
    driver.quit()
