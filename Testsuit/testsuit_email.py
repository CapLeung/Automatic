import unittest
from Testcase1.register_email import Testcase
from Test_framework.config.HTMLTestRunner import HTMLTestRunner

class Test(unittest.TestCase):
    def test_suit(self):
        my_suit = unittest.TestSuite()
        test_list = ['test_014', 'test_015', 'test_016', 'test_017', 'test_018', 'test_019']
        for case in test_list:
            my_suit.addTest(Testcase(case))

        # 生成测试报告
        with open('register_email.html', 'wb') as f:
            HTMLTestRunner(
                stream=f,
                title='email格式错误测试报告',
                description='自动化测试',
                verbosity=2
            ).run(my_suit)






