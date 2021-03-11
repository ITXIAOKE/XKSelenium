from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")

right_click = driver.find_element_by_id("su")
# 右击
ActionChains(driver).context_click(right_click).perform()
