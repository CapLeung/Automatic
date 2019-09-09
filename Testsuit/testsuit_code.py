import unittest
from Testcase1.register_code import Testcase
from Test_framework.config.HTMLTestRunner import HTMLTestRunner

class Test(unittest.TestCase):
    def test_suit(self):
        my_suit = unittest.TestSuite()
        test_list = ['test_045', 'test_046', 'test_047', 'test_048', 'test_049']
        for case in test_list:
            my_suit.addTest(Testcase(case))

        # 生成测试报告
        with open('register_code.html', 'wb') as f:
            HTMLTestRunner(
                stream=f,
                title='验证码格式错误测试报告',
                description='自动化测试',
                verbosity=2
            ).run(my_suit)






