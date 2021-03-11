from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get("http://www.126.com")
# 126网站有iframe，所以需要加以下代码，这是一个坑呀
driver.switch_to_frame('x-URS-iframe')
# driver.switch_to()

time.sleep(3)
# driver.find_element_by_xpath(".//*[@class='j-inputtext dlemail' and @type='text']").clear()
# driver.find_element_by_xpath(".//*[@class='j-inputtext dlemail' and @type='text']").send_keys("15101658189")
# time.sleep(3)
driver.find_element_by_class_name("dlemail").clear()
driver.find_element_by_class_name("dlemail").send_keys("11111")
time.sleep(3)
# driver.find_element_by_xpath(".//*[@class='j-inputtext dlpwd' and @type='password']").clear()
# driver.find_element_by_xpath(".//*[@class='j-inputtext dlpwd' and @type='password']").send_keys("15101658189")
# time.sleep(3)
driver.find_element_by_class_name("dlpwd").clear()
driver.find_element_by_class_name("dlpwd").send_keys("222222")
time.sleep(3)
driver.find_element_by_class_name("u-loginbtn").click()
# driver.find_element_by_xpath(".//*[@id='dologin']").click()
time.sleep(3)
driver.quit()
