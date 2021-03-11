from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(2)
# 输入框输入内容
# driver.find_element_by_id("kw").send_keys("seleniumm")
# time.sleep(2)
# 删除一个多余的m
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 输入空格键加一个教程关键字，空格可以乘以数字就是几个空格
driver.find_element_by_id("kw").send_keys(Keys.SPACE*4)
driver.find_element_by_id("kw").send_keys("教程")
time.sleep(2)
# ctrl+a全选
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "a")
time.sleep(2)
# ctrl+x剪切
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "x")
time.sleep(2)
# ctrl+v粘贴
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "v")
time.sleep(2)
# 回车键盘来代替点击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(2)
driver.quit()
