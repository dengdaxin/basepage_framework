import unittest
from actions.login_action import LoginAction
from common.browser_utils import BrowserUtils
from common.base_page import BasePage
from common.config_utils import Config
from actions.quit_action import QuitAction

class QuitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.basepage = BasePage(BrowserUtils().get_driver_type())
        self.basepage.max_browser()
        self.basepage.time()
        self.basepage.open_url(Config.url_path)

    def tearDown(self) -> None:
        self.basepage.close_browser_tab()

    def test_quit(self):
        login = LoginAction(self.basepage.driver)
        login.default_login()
        quit_action = QuitAction(self.basepage.driver)
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result,'系统管理员后台登录','test_quit用例执行失败')

if __name__=='__main__':
    unittest.main()