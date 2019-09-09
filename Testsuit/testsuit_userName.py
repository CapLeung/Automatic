import unittest
from Testcase1.register_userName import Testcase
from Test_framework.config.HTMLTestRunner import HTMLTestRunner

class Test(unittest.TestCase):
    def test_suit(self):
        my_suit = unittest.TestSuite()
        test_list = ['test_022', 'test_023', 'test_024', 'test_025', 'test_026', 'test_027',
                     'test_028', 'test_029', 'test_030', 'test_031', 'test_032', 'test_033', 'test_034']
        for case in test_list:
            my_suit.addTest(Testcase(case))

        # 生成测试报告
        with open('register_userName.html', 'wb') as f:
            HTMLTestRunner(
                stream=f,
                title='用户名格式错误测试报告',
                description='自动化测试',
                verbosity=2
            ).run(my_suit)






