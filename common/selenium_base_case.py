import unittest
from common.base_page import BasePage
from common.browser_utils import BrowserUtils
from common.config_utils import Config

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Config.url_path

    def setUp(self) -> None:
        self.basepage = BasePage(BrowserUtils().get_driver_type())
        self.basepage.max_browser()
        self.basepage.time()
        self.basepage.open_url(self.url)

    def tearDown(self) -> None:
        self.basepage.close_browser_tab()



