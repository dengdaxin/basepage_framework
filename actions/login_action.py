from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import Config

class LoginAction:
    def __init__(self,driver):
        self.login_page = LoginPage(driver)

    def login_action(self,username,password):
        self.login_page.input_usernames(username)
        self.login_page.input_passwords(password)
        self.login_page.click_logins()

    def login_success(self,username,password):
        self.login_action(username,password)
        #return MainPage(self.login_page.driver)

    def login_fail(self,username,password):
        self.login_action(username,password)
        self.login_page.wait(3)
        self.login_page.screentshot()

    def default_login(self):
        self.login_success(username=Config.get_default_username,password=Config.get_default_password)

