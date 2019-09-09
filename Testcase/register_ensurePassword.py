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

    def input_info(self, email, userName, password, ensure_password):
        web.input_email(email)
        web.input_userName(userName)
        web.input_password(password)
        web.input_ensure_password(ensure_password)
        web.input_code()
        # web.click('css', '.submit_reg')

    def input_info_out_ensurePassword(self, email, userName, password):
        web.input_email(email)
        web.input_userName(userName)
        web.input_password(password)
        web.input_code()
        web.click('css', '.submit_reg')

    def test_040(self):
        el = None
        web.open_url(url)
        self.input_info_out_ensurePassword('liang17@qq.com', 'lia', 'liangl')
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('重复上面所填写的密码', el)


    def test_041(self):
        el = None
        web.open_url(url)
        self.input_info(r[42][0], r[42][1], r[42][2], r[42][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('两次输入密码不一致', el)
    #     !

    def test_042(self):
        el = None
        web.open_url(url)
        self.input_info(r[43][0], r[43][1], r[43][2], r[43][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('两次输入密码不一致', el)

    def test_043(self):
        el = None
        web.open_url(url)
        self.input_info(r[44][0], r[44][1], r[44][2], r[44][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('重复上面所填写的密码', el)

    def test_044(self):
        el = None
        web.open_url(url)
        self.input_info(r[44][0], r[44][1], r[44][2], 'liang l')
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('重复上面所填写的密码', el)




