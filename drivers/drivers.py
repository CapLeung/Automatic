import time
from selenium import webdriver

class Drivers(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        # time.sleep(1)
        # self.driver.quit()

if __name__ == "__main__":
    d = Drivers()
    d.driver.get('http://localhost:8013/iwebshop/')
