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

    def input_info_outEmail(self, userName, password, ensure_password):
        web.input_userName(userName)
        web.input_password(password)
        web.input_ensure_password(ensure_password)
        web.input_code()
        web.click('css', '.submit_reg')

    def test_014(self):
        web.open_url(url)
        self.input_info(r[15][0], r[15][1], r[15][2], r[15][3])
        self.assertEqual(web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')), True)
        # html / body / div[1] / div[2] / div / div / form / table / tbody / tr[1] / td / label
        # html / body / div[1] / div[2] / div / div / form / table / tbody / tr[1] / td / label

    def test_015(self):
        web.open_url(url)
        self.input_info(r[16][0], r[16][1], r[16][2], r[16][3])
        self.assertEqual(web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')), True)

    def test_016(self):
        web.open_url(url)
        self.input_info(r[17][0], r[17][1], r[17][2], r[17][3])
        self.assertEqual(web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')), True)

    def test_017(self):
        web.open_url(url)
        self.input_info(r[18][0], r[18][1], r[18][2], r[18][3])
        self.assertEqual(web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')), True)

    def test_018(self):
        web.open_url(url)
        self.input_info('lia ng@qq.com', '啊liang_12', 'LiAng_', 'LiAng_')
        self.assertEqual(web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')), True)

    def test_019(self):
        web.open_url(url)
        self.input_info_outEmail('啊liang_13', 'LiAng_', 'LiAng_')
        # web.click('css', '.submit_reg')
        self.assertEqual(web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')), True)

