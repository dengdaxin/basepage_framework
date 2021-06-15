import os
from element_infos.login.login_page import LoginPage
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.browser_utils import BrowserUtils

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '../../webdriver/chromedriver.exe')

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        loginpage = LoginPage(driver)
        self.open_url('http://localhost/DBshop/admin')
        loginpage.input_usernames('admin')
        loginpage.input_passwords('123456')
        loginpage.click_logins()
        # self.brand = {'element_name':'后台标题',
        #               'locator_type':'xpath',
        #                 'locator_value':'//a[@class="brand"]',
        #                 'timeout':5}
        # self.count_check = {'element_name': '后台名称',
        #                     'locator_type': 'xpath',
        #                     'locator_value': '/html/body/div[1]/div/a',
        #                     'timeout': 5}
        # self.qiantai = {'element_name': '前台首页',
        #                 'locator_type': 'xpath',
        #                 'locator_value': '//a[text()="前台首页"]',
        #                 'timeout': 5}
        element = ElementdataUtils('main','main_page').get_element_info()
        self.brand = element['brand']
        self.count_check = element['count_check']
        self.qiantai = element['qiantai']
        # self.driver = loginpage.driver  #把login_page的对象转移到mainpage
        # self.brand = self.driver.find_element(By.XPATH,'//a[@class="brand"]')
        # self.count_check = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/a')
        # self.qiantai = self.driver.find_element(By.XPATH,'//a[text()="前台首页"]')

    def get_count_text(self):    #获取文本
        # value = self.count_check.text
        # logger.info('获取后台名称，后台名称是' + str(value))
        # return value
        text = self.get_text(self.count_check)
        return text

    def goto_qiantai(self):  #进入前台首页
        # self.qiantai.click()
        self.click(self.qiantai)


if __name__=='__main__':
    driver = BrowserUtils().get_driver_type()
    mainpage = MainPage(driver)
    text = mainpage.get_count_text()
    print(text)
    mainpage.goto_qiantai()
