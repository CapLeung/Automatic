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

    # 输入注册信息
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

        # 出现“请输入以下验证码”时递归
        if web.is_element_visible((By.CLASS_NAME, 'invalid-msg')) is True:
            self.input_info(email, userName, password, ensure_password)


    def test_001(self):
        web.open_url(url)
        self.input_info(r[0][0], r[0][1], r[0][2], r[0][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)
        # data = web.locateElement('xpath', ".//*[@id='artPlustipscontent']")
        # self.assertEqual('此邮箱已经被注册过，请重新更换', data)

    def test_002(self):
        web.open_url(url)
        self.input_info(r[1][0], r[1][1], r[1][2], r[1][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)
        # data = web.locateElement('xpath', ".//*[@id='artPlustipscontent']")
        # self.assertEqual('此邮箱已经被注册过，请重新更换', data)

    def test_003(self):
        web.open_url(url)
        self.input_info(r[2][0], r[2][1], r[2][2], r[2][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)
        # data = web.locateElement('xpath', ".//*[@id='artPlustipscontent']")
        # self.assertEqual('此邮箱已经被注册过，请重新更换', data)

    def test_004(self):
        web.open_url(url)
        self.input_info(r[3][0], r[3][1], r[3][2], r[3][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)
        # data = web.locateElement('xpath', ".//*[@id='artPlustipscontent']")
        # self.assertEqual('此邮箱已经被注册过，请重新更换', data)

    def test_005(self):
        web.open_url(url)
        self.input_info(r[4][0], r[4][1], r[4][2], r[4][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)

    def test_006(self):
        web.open_url(url)
        self.input_info(r[5][0], r[5][1], r[5][2], r[5][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)

    def test_007(self):
        web.open_url(url)
        self.input_info(r[6][0], r[6][1], r[6][2], r[6][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)

    def test_008(self):
        web.open_url(url)
        self.input_info(r[7][0], r[7][1], r[7][2], r[7][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)

    def test_009(self):
        web.open_url(url)
        self.input_info(r[8][0], r[8][1], r[8][2], r[8][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)

    def test_010(self):
        web.open_url(url)
        self.input_info(r[9][0], r[9][1], r[9][2], r[9][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)

    def test_011(self):
        web.open_url(url)
        self.input_info(r[10][0], r[10][1], r[10][2], r[10][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)

    def test_012(self):
        web.open_url(url)
        self.input_info(r[11][0], r[11][1], r[11][2], r[11][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)

    def test_013(self):
        web.open_url(url)
        self.input_info(r[12][0], r[12][1], r[12][2], r[12][3])
        data = web.locateElement('class_name', 'f14').text
        self.assertEqual('恭喜，操作成功！', data)

    # 邮箱格式错误
    def test_014(self):
        web.open_url(url)
        self.input_info(r[13][0], r[13][1], r[13][2], r[13][2])
        self.assertEqual(web.is_element_visible((By.CSS_SELECTOR, '.invalid-msg')), 'True')

# if __name__ == '__main__':
#     unittest.main()
    # print(type(r[0][0]))
    # print(r[1])
    # print(r[2])



