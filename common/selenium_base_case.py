import unittest
from common.base_page import BasePage
from common.browser_utils import BrowserUtils
from common.config_utils import Config
from common.log_utils import logger

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info('======测试类开始执行=====')
        cls.url = Config.url_path

    def setUp(self) -> None:
        logger.info('-----测试开始执行-----')
        self.basepage = BasePage(BrowserUtils().get_driver_type())
        self.basepage.max_browser()
        self.basepage.time()
        self.basepage.open_url(self.url)

    def tearDown(self) -> None:
        logger.info('-----测试方法执行完毕-----')
        self.basepage.close_browser_tab()

    # def tearDownClass(cls) -> None:
    #     logger.info('======测试类执行完毕=====')

