from element_infos.main.main_page import MainPage
from element_infos.login.login_page import LoginPage
class QuitAction:
    def __init__(self,driver):
        self.main_page = MainPage(driver)

    def quit(self):
        self.main_page.quit_system()
        return LoginPage(self.main_page.driver)