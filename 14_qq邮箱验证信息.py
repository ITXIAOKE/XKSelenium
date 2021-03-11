from selenium import webdriver
import time

# qq空间登录
driver = webdriver.Firefox()
driver.get("https://mail.qq.com")
# 加iframe
frame = driver.find_element_by_id("login_frame")
driver.switch_to.frame(frame)

# 设置浏览器窗口的位置和大小
driver.set_window_position(75, 15)
driver.set_window_size(1100, 700)

title = driver.title
print("登录前标题为：{}".format(title))
time.sleep(2)
cur_url = driver.current_url
print("登录前url为：%s" % cur_url)

time.sleep(2)

# 通过使用选择器选择到表单元素进行模拟输入和点击按钮提交switcher_plogin
driver.find_element_by_id("switcher_plogin").click()
time.sleep(2)
driver.find_element_by_id("u").clear()
driver.find_element_by_id("u").send_keys("976249817")
time.sleep(2)
driver.find_element_by_id("p").clear()
driver.find_element_by_id("p").send_keys("cxz")
time.sleep(2)
driver.find_element_by_id("login_button").click()
time.sleep(2)

title = driver.title
print("登录后标题为：{}".format(title))
time.sleep(2)
cur_url = driver.current_url
print("登录后url为：%s" % cur_url)
time.sleep(2)

name = driver.find_element_by_xpath(".//*[@id='useraddr']").text
print("用户名为:%s" % name)
time.sleep(2)
# 退出窗口
driver.quit()
