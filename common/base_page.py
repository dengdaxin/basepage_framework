import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains  #鼠标键盘
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.config_utils import Config
from common.log import logger

current_path = os.path.dirname(__file__)
current_dir = os.path.join(current_path,'..')
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    #浏览器操作封装
    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开url地址：%s' % url)

    def close_browser_tab(self):
        self.driver.close()
        logger.info('关闭当前tab页')

    def exit_browser(self):
        self.driver.quit()
        logger.info('退出浏览器')

    def max_browser(self):
        self.driver.maximize_window()
        logger.info('最大化浏览器')

    def min_browser(self):
        self.driver.minimize_window()
        logger.info('最小化浏览器')

    def time(self,seconds=Config.time_out):
        '''隐式等待'''
        self.driver.implicitly_wait(seconds)

    def refresh(self):
        self.driver.refresh()
        logger.info('刷新浏览器')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题,标题是:%s'%value)
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

    def move_to_element_by_mouse(self,element_info):
        '''移动鼠标到指定元素位置'''
        element = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()

    def long_press_element(self,element_info,senconds):
        '''模拟鼠标长按指定时间后释放'''
        element = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(element).pause(senconds).release(element)

    def switch_to_frame(self,element_info):
        '''frame切换'''
        element = self.find_element(element_info)
        self.driver.switch_to_frame(element)

    def screentshot(self,*screentshot_path):
        '''截图封装'''
        if len(screentshot_path) == 0:
            screentshot_filepath = Config.screentshot_path
        else:
            screentshot_filepath = screentshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        screentshot_filepath = os.path.join(current_dir,screentshot_filepath,'UiTtest_%s.png' % now)
        self.driver.get_screenshot_as_file(screentshot_filepath)

    def wait(self,seconds=Config.time_out):
        '''固定等待'''
        time.sleep(seconds)


    # def input(self, element_info, content):
    #     try:
    #         element = self.find_element(element_info)
    #         element.send_keys(content)
    #         logger.info('[%s]元素输入数据%s' % (element_info['element_name'], content))
    #     except Exception as e:
    #         logger.error('[%s]元素输入数据失败，原因是：%s' % (element_info['element_name'], e.__str__()))