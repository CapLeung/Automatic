import time
# -*- coding: utf-8 -*-

from Test_framework.drivers.drivers import Drivers
from PIL import Image
import pytesseract
from selenium.webdriver.support import expected_conditions as EC

class Common(Drivers):
    # 打开链接
    def open_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    # 元素定位
    def locateElement(self, locate_type, value):
        el = None
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        if locate_type == 'name':
            el = self.driver.find_element_by_name(value)
        if locate_type == 'class_name':
            el = self.driver.find_element_by_class_name(value)
        if locate_type == 'tag_name':
            el = self.driver.find_element_by_tag_name(value)
        if locate_type == 'link_text':
            el = self.driver.find_element_by_link_text(value)
        if locate_type == 'partial':
            el = self.driver.find_element_by_partial_link_text(value)
        if locate_type == 'css':
            el = self.driver.find_element_by_css_selector(value)
        if locate_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)

        if el is not None:
            return el

    # 点击
    def click(self, locate_type, value):
        el = self.locateElement(locate_type, value)
        el.click()

    # 输入数据
    def input_data(self, locate_type, value, text):
        el = self.locateElement(locate_type, value)
        el.send_keys(text)

    # 获取属性值
    def get_att(self, locate_type, value, att_name):
        el = self.locateElement(locate_type, value)
        return el.get_attribute(att_name)

    def clear(self, locate_type, value):
        el = self.locateElement(locate_type, value)
        el.clear()

    # 截图
    def screen_shot(self):
        filename = '../Testcase/image.png'
        self.driver.save_screenshot(filename)
        element = self.locateElement('css', '#captchaImg')
        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']
        # 打开刚才的截图
        im = Image.open(filename)
        # 截取对应位置
        im = im.crop((left, top, right, bottom))
        # 保存覆盖原有截图
        im.save(filename)

        image = Image.open('../Testcase/image.png')
        content = pytesseract.image_to_string(image)  # 解析图片
        return content

    # 识别图片
    def circle(self):
        self.click('css', '.link')
        content = self.screen_shot()
        # print(content)
        pan = 0

        while content is None or len(content) != 5 or pan < 5:
            self.click('css', '.link')
            content = self.screen_shot()
            # print(content)
            for i in content:
                if i.isalpha():
                    pan += 1
        print(content)
        return content

    # 判断元素是否可见
    def is_element_visible(self, element):
        driver = self.driver
        try:
            the_element = EC.visibility_of_element_located(element)
            assert the_element(driver)
            flag = True
        except:
            flag = False
        return flag


    # 输入邮箱
    def input_email(self, email):
        el = self.locateElement('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td/input')
        el.clear()
        el.send_keys(email)

    # 输入用户名
    def input_userName(self, userName):
        el = self.locateElement('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[2]/td/input')
        el.clear()
        el.send_keys(userName)

    # 输入设置密码
    def input_password(self, password):
        el = self.locateElement('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[3]/td/input')
        el.clear()
        el.send_keys(password)

    # 输入确认密码
    def input_ensure_password(self, ensure_password):
        el = self.locateElement('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[4]/td/input')
        el.clear()
        el.send_keys(ensure_password)

    # 输入错误验证码
    def input_wrongCode(self, code):
        el = self.locateElement('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[5]/td/input')
        el.click()
        el.send_keys(code)

    # 输入验证码
    def input_code(self):
        content = self.circle()
        el = self.locateElement('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[5]/td/input')
        el.clear()
        el.send_keys(content)

    # def __del__(self):
    #     time.sleep(1)
    #     self.driver.close()
"""
        if content is not None and len(content) == 5:
            for i in content:
                if not i.isalpha():
                    pan = False
            if pan is True and len(content) != 0:
                print(content)
                return content
            else:
                self.circle()
        else:
            # print(content)
            self.circle()
"""






if __name__ == '__main__':
    web = Common()
    # web.open_url('http://localhost:8013/iwebshop/index.php?controller=simple&action=reg')
    # web.locateElement('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td/input').send_keys('976673947@qq.com')
    # web.driver.find_element_by_xpath('html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td/input').send_keys('4444')
    # web.click('css', '.submit_reg')
    # web.input_data('xpath', 'html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td/input', '1224847886@qq.com')



