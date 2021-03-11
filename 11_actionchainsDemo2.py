from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
# time.sleep(3)
# move = driver.find_element_by_xpath(".//*[@id='u1']/a[8]")
# move = driver.find_element_by_link_text("设置")
#
# move=driver.find_element_by_class_name("pf pfhover")
# time.sleep(3)
# 悬停
# ActionChains(driver).move_to_element(move).perform()


# 双击操作
double_click = driver.find_element_by_xpath(".//*[@id='u1']/a[3]")
ActionChains(driver).double_click(double_click).perform()

# 鼠标拖拽推放操作
# element = driver.find_element_by_id("aa")
# target = driver.find_element_by_id("bb")
# ActionChains(driver).drag_and_drop(element, target).perform()
