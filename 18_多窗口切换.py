from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
time.sleep(2)
# 获得百度搜索窗口句柄
search_handler = driver.current_window_handle
print(search_handler)

driver.find_element_by_link_text("登录").click()
time.sleep(2)
# driver.switch_to.alert
print("111111111111")
# print(driver.find_element_by_link_text("立即注册").find_element_by_name("href"))
# aa = driver.find_element_by_css_selector(".pass-reglink")
# aa = driver.find_element_by_xpath(".//*[@id='passport-login-pop-dialog']/div/div/div/div[3]/a")
# driver.find_element_by_link_text("立即注册").find_element_by_xpath(
#     ".//*[@id='passport-login-pop-dialog']/div/div/div/div[3]/a").click()
driver.find_element_by_link_text("立即注册").click()
# ActionChains(driver).double_click(aa).perform()

# driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
# driver.find_element_by_link_text("用户名登录").click()
# driver.find_element_by_class_name("tang-pass-footerBarULogin").click()
time.sleep(2)
all_handlers = driver.window_handles
print(all_handlers)

# 进入注册窗口
for handler in all_handlers:
    if handler != search_handler:
        driver.switch_to.window(handler)
        time.sleep(3)
        driver.find_element_by_name("userName").send_keys("aaa")
        # driver.find_element_by_name("password").send_keys("111")
        driver.close()

# 进入搜索框窗口
for handler in all_handlers:
    if handler == search_handler:
        driver.switch_to.window(handler)
        time.sleep(3)
        driver.find_element_by_css_selector("#TANGRAM__PSP_4__closeBtn").click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

driver.quit()
