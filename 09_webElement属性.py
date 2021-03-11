from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://www.baidu.com")

size = driver.find_element_by_xpath(".//*[@id='kw']").size
print("窗口大小为：%s" % size)

text = driver.find_element_by_id('cp').text
print("百度首页底部信息为：%s" % text)

attr = driver.find_element_by_id('kw').get_attribute('class')
print("元素属性的值为：%s" % attr)

flag = driver.find_element_by_id('kw').is_displayed()
print("返回元素的结果是否可见：%s" % flag)

driver.quit()
