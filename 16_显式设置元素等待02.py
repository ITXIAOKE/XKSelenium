from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
input_ = driver.find_element_by_id("kw")

# 超时时间设置为5秒，时间步长为0.5秒
# lambda表达式：冒号前是参数，冒号后是表达式
# is_displayed()判断输入框是否可见
element = WebDriverWait(driver, 5, 0.5).until(
    lambda bol: input_.is_displayed()
)

# input_输入框如果可见，就输入关键字
input_.send_keys("selenium")

driver.quit()
