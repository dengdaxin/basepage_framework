import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.log import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    #浏览器操作封装
    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开url地址：%s' % url)

    def max_browser(self):
        self.driver.maximize_window()
        logger.info('最大化浏览器')

    def min_browser(self):
        self.driver.minimize_window()
        logger.info('最小化浏览器')

    def refresh(self):
        self.driver.refresh()
        logger.info('刷新浏览器')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题,标题是%s'%value)
        return value
    #元素操作封装
    def find_element(self,element_info):

        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        elif locator_type_name == 'css':
            locator_type = By.CSS_SELECTOR
        elif locator_type_name == 'link':
            locator_type = By.LINK_TEXT
        elif locator_type_name == 'tag_name':
            locator_type = By.TAG_NAME
        elif locator_type_name == 'name':
            locator_type = By.NAME
        element = WebDriverWait(self.driver, locator_timeout).until(lambda x: x.find_element(locator_type, locator_value_info))
        logger.info('[%s]元素识别成功' % element_info['element_name'] )
        return element

    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]元素点击操作成功' % element_info['element_name'])

    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容成功，输入的内容是：%s' % (element_info['element_name'],content) )

    def get_text(self,element_info):
        element = self.find_element(element_info)
        text = element.text
        logger.info('获取元素文本，文本为%s'% text)
        return text
    # def input(self, element_info, content):
    #     try:
    #         element = self.find_element(element_info)
    #         element.send_keys(content)
    #         logger.info('[%s]元素输入数据%s' % (element_info['element_name'], content))
    #     except Exception as e:
    #         logger.error('[%s]元素输入数据失败，原因是：%s' % (element_info['element_name'], e.__str__()))