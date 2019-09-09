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

    def input_info_outPassword(self, email, userName, ensure_password):
        web.input_email(email)
        web.input_userName(userName)
        web.input_ensure_password(ensure_password)
        web.input_code()
        web.click('css', '.submit_reg')

    def test_036(self):
        el = None
        web.open_url(url)
        self.input_info(r[36][0], r[36][1], r[36][2], r[36][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写6-32个字符', el)


    def test_037(self):
        el = None
        web.open_url(url)
        self.input_info(r[37][0], r[37][1], r[37][2], r[37][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写6-32个字符', el)

    def test_038(self):
        el = None
        web.open_url(url)
        self.input_info_outPassword('liang15@qq.com', 'lia', 'liangl')
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写6-32个字符', el)

    def test_039(self):
        el = None
        web.open_url(url)
        self.input_info('liang16@qq.com', 'lia', 'liang l', 'liang l')
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写6-32个字符', el)



