from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
time.sleep(2)
# 获得百度搜索窗口句柄
search_handler = driver.current_window_handle
print(search_handler)

driver.find_element_by_link_text("登录").click()
time.sleep(2)
# driver.current_window_handle
driver.switch_to.window(driver.current_window_handle)
print("111111111111")
print(
    driver.find_element_by_xpath(".//*[@id='passport-login-pop']").get_attribute(
        "class"))

aa = driver.find_element_by_xpath(".//*[@id='passport-login-pop']/div[2]/div[2]/div/div/div/div/div[3]/a")

ActionChains(driver).click(aa).perform()
time.sleep(2)
all_handlers = driver.window_handles
print(all_handlers)

# 进入注册窗口
for handler in all_handlers:
    if handler != search_handler:
        driver.switch_to.window(handler)
        driver.find_element_by_name("userName").send_keys("aaa")
        driver.find_element_by_name("password").send_keys("111")
        driver.close()

# 进入搜索框窗口
for handler in all_handlers:
    if handler == search_handler:
        driver.switch_to.window(handler)
        driver.find_element_by_css_selector("#TANGRAM__PSP_4__closeBtn").click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

driver.quit()
