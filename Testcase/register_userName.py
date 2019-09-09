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

    def input_info_outUserName(self, email, password, ensure_password):
        web.input_email(email)
        web.input_password(password)
        web.input_ensure_password(ensure_password)
        web.input_code()
        web.click('css', '.submit_reg')

    def test_022(self):
        el = None
        web.open_url(url)
        self.input_info(r[22][0], r[22][1], r[22][2], r[22][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_023(self):
        el = None
        web.open_url(url)
        self.input_info(r[23][0], r[23][1], r[23][2], r[23][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_024(self):
        el = None
        web.open_url(url)
        self.input_info(r[24][0], r[24][1], r[24][2], r[24][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_025(self):
        el = None
        web.open_url(url)
        self.input_info(r[25][0], r[25][1], r[25][2], r[25][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_026(self):
        el = None
        web.open_url(url)
        self.input_info(r[26][0], r[26][1], r[26][2], r[26][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_027(self):
        el = None
        web.open_url(url)
        self.input_info(r[27][0], r[27][1], r[27][2], r[27][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_028(self):
        el = None
        web.open_url(url)
        self.input_info(r[28][0], r[28][1], r[28][2], r[28][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_029(self):
        el = None
        web.open_url(url)
        self.input_info(r[29][0], r[29][1], r[29][2], r[29][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_030(self):
        el = None
        web.open_url(url)
        self.input_info(r[30][0], r[30][1], r[30][2], r[30][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_031(self):
        el = None
        web.open_url(url)
        self.input_info(r[31][0], r[31][1], r[31][2], r[31][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_032(self):
        el = None
        web.open_url(url)
        self.input_info(r[32][0], r[32][1], r[32][2], r[32][3])
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_033(self):
        el = None
        web.open_url(url)
        self.input_info('liang13@163.com', 'liang a', 'LiAng_', 'LiAng_')
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)

    def test_034(self):
        el = None
        web.open_url(url)
        self.input_info_outUserName('liang13@163.com', 'LiAng_', 'LiAng_')
        if web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')) is True:
            el = web.locateElement('css', '.invalid-msg').text
        self.assertEqual('填写2-20个字符，可以为字数，数字下划线和中文', el)





