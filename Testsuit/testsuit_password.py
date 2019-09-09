import unittest
from Testcase1.register_password import Testcase
from Test_framework.config.HTMLTestRunner import HTMLTestRunner

class Test(unittest.TestCase):
    def test_suit(self):
        my_suit = unittest.TestSuite()
        test_list = ['test_036', 'test_037', 'test_038', 'test_039']
        for case in test_list:
            my_suit.addTest(Testcase(case))

        # 生成测试报告
        with open('register_password.html', 'wb') as f:
            HTMLTestRunner(
                stream=f,
                title='设置密码格式错误测试报告',
                description='自动化测试',
                verbosity=2
            ).run(my_suit)






