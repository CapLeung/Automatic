from selenium.webdriver.common.by import By
import unittest
from Test_framework.utils.common import Common
from Test_framework.config.HTMLTestRunner import HTMLTestRunner

web = Common()
url = 'http://localhost:8013/iwebshop/index.php?controller=simple&action=reg'


class Testcase(unittest.TestCase):
    def setUp(self):
        print('开始')

    def tearDown(self):
        print('结束')

    def input_info(self, email, userName, password, ensure_password):
        web.input_email(email)
        web.input_userName(userName)
        web.input_password(password)
        web.input_ensure_password(ensure_password)
        web.input_code()
        web.click('css', '.submit_reg')
        if web.is_element_visible((By.XPATH, ".//*[@id='artPlustipscontent']")) is True:
            el = web.locateElement('xpath', ".//*[@id='artPlustipscontent']").text
            if el == '验证码输入不正确':
                self.input_info(email, userName, password, ensure_password)
            elif el == '此邮箱已经被注册过，请重新更换':
                return ''
        if web.is_element_visible((By.CLASS_NAME, 'invalid-msg')) is True:
            self.input_info(email, userName, password, ensure_password)

    def test_001(self):
        web.open_url(url)
        self.input_info('12@dao.com', 'lllblh47hh1', '123456', '123456')
        # data = web.locateElement('class_name', 'f14').text
        # self.assertEqual('恭喜，操作成功！', data)
        data = web.locateElement('xpath', ".//*[@id='artPlustipscontent']")
        self.assertEqual('此邮箱已经被注册过，请重新更换', data)

    def test_002(self):
        web.open_url(url)
        self.input_info('123182@1.com', 'llahhh454', '1234567', '1234567')
        # data = web.locateElement('class_name', 'f14').text
        # self.assertEqual('恭喜，操作成功！', data)
        data = web.locateElement('xpath', ".//*[@id='artPlustipscontent']")
        self.assertEqual('此邮箱已经被注册过，请重新更换', data)

    def test_003(self):
        web.open_url(url)
        self.input_info('123a182@sina.com', '啊哈lalahhh45641', '134567', '134567')
        # data = web.locateElement('class_name', 'f14').text
        # self.assertEqual('恭喜，操作成功！', data)
        data = web.locateElement('xpath', ".//*[@id='artPlustipscontent']")
        self.assertEqual('此邮箱已经被注册过，请重新更换', data)


if __name__ == '__main__':
    unittest.main()




