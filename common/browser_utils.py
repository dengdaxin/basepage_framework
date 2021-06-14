import os
from selenium import webdriver
from common.config_utils import Config

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path,'..' + Config.driver_path)

class BrowserUtils():
    def __init__(self,driver_path=driver_path):
        self.driver_path = driver_path

    def get_chrome_driver(self):
        chromedriver_path = os.path.join(driver_path,'chromedriver.exe')
        driver = webdriver.Chrome(chromedriver_path)
        return driver

    def get_firefox_driver(self):
        firefoxdriver_path = os.path.join(driver_path,'geckodriver.exe')
        driver = webdriver.Firefox(executable_path=firefoxdriver_path)
        return driver

    def get_ie_driver(self):
        iedriver_path = os.path.join(driver_path,'IEDriverServer.exe')
        driver = webdriver.Ie(iedriver_path)
        return driver