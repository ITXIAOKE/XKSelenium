import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import HtmlTestRunner


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_func(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("wd").clear()
        driver.find_element_by_name("wd").send_keys("selenium")
        driver.find_element_by_id("su").click()

        # 等待元素的显示
        for i in range(6):
            try:
                if u"selenium_百度搜索" == driver.title:
                    break
            except Exception as e:
                print(e)
            time.sleep(1)
        else:
            self.fail("time out")

        # 断言
        self.assertEqual("", driver.find_element_by_css_selector(u'img[alt=\"到百度首页\"]').text)

        # 验证
        # 验证失败是不影响后面脚本的执行
        # 断言失败是影响后面脚本的执行
        try:
            self.assertEqual(u"selenium_百度搜索", driver.title)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # 第二次的百度搜索
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium2")
        driver.find_element_by_id("su").click()

    # 判断元素是否存在
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            print(e)
            return False
        return True

    # 判断对话框是否存在
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            print(e)
            return False
        return True

    @unittest.skip("this is skip")
    def test_htmltestrunner(self):
        pass

    def close_alert_and_get_its_next(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="baidu22", descriptions=u"百度测试报告", report_title=u"各个用例执行情况"))
