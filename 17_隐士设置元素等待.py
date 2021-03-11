from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 等待10秒后，还没有找到该元素，就抛出NoSuchElementException异常信息
driver.implicitly_wait(10)

driver.find_element_by_id("kw11").send_keys("selenium")

driver.quit()
