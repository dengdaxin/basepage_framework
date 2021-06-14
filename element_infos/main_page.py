import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_infos.login_page import LoginPage
from common.log import logger
current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')

class MainPage():
    def __init__(self):

        loginpage = LoginPage()
        loginpage.input_username('admin')
        loginpage.input_password('123456')
        loginpage.click_login()
        self.driver = loginpage.driver  #把login_page的对象转移到mainpage
        self.brand = self.driver.find_element(By.XPATH,'//a[@class="brand"]')
        self.count_check = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/a')
        self.qiantai = self.driver.find_element(By.XPATH,'//a[text()="前台首页"]')

    def get_count_text(self):    #获取文本
        value = self.count_check.text
        logger.info('获取后台名称，后台名称是' + str(value))
        return value

    def goto_qiantai(self):  #进入前台首页
        self.qiantai.click()


if __name__=='__main__':
    mainpage = MainPage()
    text = mainpage.get_count_text()
    print(text)
    mainpage.goto_qiantai()
