import unittest
from actions.login_action import LoginAction
from common.browser_utils import BrowserUtils
from common.base_page import BasePage
from common.config_utils import Config

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.basepage = BasePage(BrowserUtils().get_driver_type())
        self.basepage.max_browser()
        self.basepage.time()
        self.basepage.open_url(Config.url_path)

    def tearDown(self) -> None:
        self.basepage.close_browser_tab()

    def test_login_success(self):
        login_action = LoginAction(self.basepage.driver)
        login_action.login_success('admin','123456')
        self.assertEqual('admin','admin','test_login_success用例执行失败')

if __name__=='__main__':
    unittest.main()