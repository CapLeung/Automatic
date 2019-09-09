from selenium.webdriver.common.by import By
import unittest
from Test_framework.utils.common import Common
from Test_framework.utils.ReadCsv import ReadCsv

read = ReadCsv()
r = read.read_csv('../Test_framework/data/register.csv')
web = Common()
url = 'http://localhost:8013/iwebshop/index.php?controller=simple&action=reg'

class Testcase(unittest.TestCase):
    def setUp(self):
        print('开始')

    def tearDown(self):
        print('结束')

    def input_info(self, email, userName, password, ensure_password, code):
        web.input_email(email)
        web.input_userName(userName)
        web.input_password(password)
        web.input_ensure_password(ensure_password)
        web.input_wrongCode(code)
        web.click('css', '.submit_reg')

    def input_info_out_code(self, email, userName, password, ensure_password):
        web.input_email(email)
        web.input_userName(userName)
        web.input_password(password)
        web.input_ensure_password(ensure_password)
        # web.input_code()
        web.click('css', '.submit_reg')

    def test_045(self):
        el = None
        web.open_url(url)
        self.input_info('liang22@qq.com', 'lia', 'liangl', 'liangl', 'abcde')
        if web.is_element_visible((By.XPATH, ".//*[@id='artPlustipscontent']")) is True:
            el = web.locateElement('xpath', ".//*[@id='artPlustipscontent']").text
        self.assertEqual('验证码输入不正确', el)


    def test_046(self):
        el = None
        web.open_url(url)
        self.input_info('liang22@qq.com', 'lia', 'liangl', 'liangl', 'aasdjaldjasda')
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写下面图片所示的字符', el)
    #     !

    def test_047(self):
        el = None
        web.open_url(url)
        self.input_info('liang22@qq.com', 'lia', 'liangl', 'liangl', 'dada@')
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写下面图片所示的字符', el)

    def test_048(self):
        el = None
        web.open_url(url)
        self.input_info('liang22@qq.com', 'lia', 'liangl', 'liangl', 'abc de')
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写下面图片所示的字符', el)

    def test_049(self):
        el = None
        web.open_url(url)
        self.input_info_out_code('liang22@qq.com', 'lia', 'liangl', 'liangl')
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写下面图片所示的字符', el)




