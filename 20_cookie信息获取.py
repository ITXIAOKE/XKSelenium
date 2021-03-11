from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.add_cookie({"name": "1111", "value": "2222"})

# print(driver.get_cookies())
for cookie in driver.get_cookies():
    print(cookie)

driver.quit()
