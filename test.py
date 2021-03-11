from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
time.sleep(2)
# 获得百度搜索窗口句柄
search_handler = driver.current_window_handle
print(search_handler)
time.sleep(2)
print(driver.find_element(By.NAME, "tj_trnews").get_attribute("href"))

driver.find_element_by_link_text("登录").click()
time.sleep(2)
# driver.switch_to_window(driver.current_window_handle)
aa = driver.find_element_by_xpath(".//*[@id='passport-login-pop-dialog']/div/div/div/div[3]/a")
ActionChains(driver).double_click(aa).perform()
print(driver.find_element_by_link_text("立即注册").get_attribute("href"))
# driver.switch_to.alert
# print("111111111111")
# aa = driver.find_element_by_css_selector("#TANGRAM__PSP_4__closeBtn")
# bb = driver.find_element_by_id("TANGRAM__PSP_4__closeBtn")
# aa = driver.find_element_by_css_selector(".pass-reglink")
# aa = driver.find_element_by_link_text("立即注册")
# aa = driver.find_element_by_xpath(".//*[@id='passport-login-pop-dialog']/div/div/div/div[3]/a")
# ActionChains(driver).double_click(bb).perform()

# driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
# driver.find_element_by_link_text("用户名登录").click()
# driver.find_element_by_class_name("tang-pass-footerBarULogin").click()
