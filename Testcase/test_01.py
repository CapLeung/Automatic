# -*- coding:utf-8 -*-
import time
import unittest
from Test_framework.utils.common import Common

from PIL import Image
import pytesseract
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# class Register(unittest.TestCase):
#
#     def setUp(self):
#         print('开始')
#
#     def tearDown(self):
#         print('结束')
#
#     def test_001(self):
#         web = Common()
#         web.open_url('http://localhost:8013/iwebshop/index.php?controller=simple&action=reg')




if __name__ == '__main__':
    # main()
    # 邮箱    用户名 输入密码  确认密码    验证码
    def password():
        web.clear('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td/input')
        web.input_data('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td/input', '123@qq.com')
        web.clear('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[2]/td/input')
        web.input_data('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[2]/td/input', '啊哈哈哈哈')
        web.clear('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[3]/td/input')
        web.input_data('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[3]/td/input', '123456')
        web.clear('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[4]/td/input')
        web.input_data('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[4]/td/input', '123456')
        web.clear('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[5]/td/input')
        content = web.circle()
        # print(content)
        # content = content.encode('utf-8')
        web.input_data('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[5]/td/input', content)
        time.sleep(1)
        web.click('css', '.submit_reg')

        """<div id="artPlustipscontent" class="aui_content">验证码输入不正确</div>"""
        """<div id="artPlustipscontent" class="aui_content">此邮箱已经被注册过，请重新更换</div>"""
        if web.is_element_visible((By.XPATH, ".//*[@id='artPlustipscontent']")) is True:
            el = web.locateElement('xpath', ".//*[@id='artPlustipscontent']").text
            if el == '验证码输入不正确':
                password()
            elif el == '此邮箱已经被注册过，请重新更换':
                return ''

        if web.is_element_visible((By.CLASS_NAME, 'invalid-msg')) is True:
            password()





    web = Common()
    web.open_url('http://localhost:8013/iwebshop/index.php?controller=simple&action=reg')
    password()






