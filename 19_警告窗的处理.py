from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

aa = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(aa).perform()

# 打开搜索设置
driver.find_element_by_class_name("setpref").click()
sleep(2)
# 保存设置
driver.find_element_by_css_selector(".prefpanelgo").click()
sleep(2)
# 接收弹窗
driver.switch_to.alert.accept()
sleep(2)

driver.quit()



