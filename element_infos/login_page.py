import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log import logger
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.browser_utils import BrowserUtils

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.input_username = {'element_name':'用户名输入框',
        #                        'locator_type':'xpath',
        #                        'locator_value':'//input[@id="user_name"]',
        #                        'timeout':5}
        # self.input_password = {'element_name':'密码输入框',
        #                        'locator_type':'xpath',
        #                        'locator_value':'//input[@id="user_passwd"]',
        #                        'timeout':5}
        # self.click_login = {'element_name': '登录按钮',
        #                        'locator_type':'xpath',
        #                        'locator_value':'//button[@type="submit"]',
        #                        'timeout':5}
        # self.driver = webdriver.Chrome(executable_path=driver_path)
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        # self.driver.get('http://localhost/DBshop/admin')
        # self.username_input = self.driver.find_element(By.XPATH,'//input[@id="user_name"]')   #属性==  页面上的控件
        # self.password_input = self.driver.find_element(By.XPATH,'//input[@id="user_passwd"]')
        # self.login_button = self.driver.find_element(By.XPATH,'//button[@type="submit"]')
        element = ElementdataUtils('login_page').get_element_info()
        self.input_username = element['input_username']
        self.input_password = element['input_password']
        self.click_login = element['click_login']

    def input_usernames(self,username):    #方法==    空间的操作
        self.input(self.input_username,username)
        # self.username_input.send_keys(username)
        # logger.info('输入用户名：' + str(username))
    def input_passwords(self,password):
        # self.password_input.send_keys(password)
        # logger.info('输入密码：' + str(password))
        self.input(self.input_password,password)

    def click_logins(self):
        # self.login_button.click()
        # logger.info('点击登录按钮')
        self.click(self.click_login)

if __name__=='__main__':
    # current_path = os.path.dirname(__file__)
    # driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')
    # driver = webdriver.Chrome(executable_path=driver_path)
    driver = BrowserUtils().get_chrome_driver()
    loginpage = LoginPage(driver)
    loginpage.open_url('http://localhost/DBshop/admin')
    loginpage.input_usernames('admin')
    loginpage.input_passwords('123456')
    loginpage.click_logins()