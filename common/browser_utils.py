import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.config_utils import Config

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path,'..' + Config.driver_path)

class BrowserUtils():
    def __init__(self,driver_path=driver_path,driver_type=Config.driver_type):
        self.__driver_path = driver_path
        self.__driver_type = driver_type

    def get_driver_type(self):
        '''封装默认浏览器，想用其他浏览器测试，只需要在ini更换'''
        if self.__driver_type == 'chrome':
            return self.__get_chrome_driver()
        elif self.__driver_type == 'firefox':
            return self.__get_firefox_driver()
        elif self.__driver_type == 'ie':
            return self.__get_ie_driver()
        elif self.__driver_type == 'edge':
            return self.__get_edge_driver()

    def __get_chrome_driver(self): #私有方法
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8') #设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension',False) #取消chrome受自动化工具的提示
        chrome_options.add_experimental_option('excludeSwitches',['enable-automation']) #取消chrome受自动化工具的提示
        chromedriver_path = os.path.join(driver_path,'chromedriver.exe')
        driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver_path)
        return driver

    def __get_firefox_driver(self):
        firefoxdriver_path = os.path.join(driver_path,'geckodriver.exe')
        driver = webdriver.Firefox(executable_path=firefoxdriver_path)
        return driver

    def __get_ie_driver(self):
        iedriver_path = os.path.join(driver_path,'IEDriverServer.exe')
        driver = webdriver.Ie(executable_path=iedriver_path)
        return driver

    def __get_edge_driver(self):
        edgedriver_path = os.path.join(driver_path,'msedgedriver.exe')
        driver = webdriver.Edge(executable_path=edgedriver_path)
        return driver