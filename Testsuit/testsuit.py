import unittest
from Testcase1.register_success import Testcase
from Test_framework.config.HTMLTestRunner import HTMLTestRunner

class Test(unittest.TestCase):
    def test_suit(self):
        my_suit = unittest.TestSuite()
        test_list = ['test_001', 'test_002', 'test_003', 'test_004', 'test_005', 'test_006',
                     'test_007', 'test_008', 'test_009', 'test_010', 'test_011', 'test_012',
                     'test_013']
        for case in test_list:
            my_suit.addTest(Testcase(case))

        # 生成测试报告
        with open('register_sucess.html', 'wb') as f:
            HTMLTestRunner(
                stream=f,
                title='注册成功测试报告',
                description='自动化测试',
                verbosity=2
            ).run(my_suit)






