import unittest
from actions.login_action import LoginAction
from common.browser_utils import BrowserUtils
from common.base_page import BasePage
from common.config_utils import Config
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils

class LoginTest(SeleniumBaseCase):
    # def setUp(self) -> None:
    #     self.basepage = BasePage(BrowserUtils().get_driver_type())
    #     self.basepage.max_browser()
    #     self.basepage.time()
    #     self.basepage.open_url(Config.url_path)
    #
    # def tearDown(self) -> None:
    #     self.basepage.close_browser_tab()
    test_class_data = TestDataUtils('login_suite', 'LoginTest').convert_exceldata_to_testdata()
    def setUp(self) -> None:
        super().setUp()
        #self.test_class_data = TestDataUtils('login_suite','LoginTest').convert_exceldata_to_testdata()

    @unittest.skipIf(test_class_data['test_login_success']['isnot'],'')  #跳过该测试方法
    def test_login_success(self):
        test_data = self.test_class_data['test_login_success']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.basepage.driver)
        main_page = login_action.login_success(test_data['test_parameter'].get('username'),test_data['test_parameter'].get('password'))
        value = main_page.get_count_text()
        self.assertEqual(value,test_data['excepted_result'],'test_login_success用例执行失败')

    @unittest.skipIf(test_class_data['test_login_fail']['isnot'], '')
    def test_login_fail(self):
        test_data = self.test_class_data['test_login_fail']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.basepage.driver)
        login_action.login_fail(test_data['test_parameter'].get('username'),test_data['test_parameter'].get('password'))
        self.assertEqual('测试',test_data['excepted_result'],'test_login_fail测试失败')

if __name__=='__main__':
    unittest.main()