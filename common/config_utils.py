import os
import time
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path,'../conf/config.ini')

class ConfigUtils:
    def __init__(self,config_path=config_path):
        self.__conf = configparser.ConfigParser()
        self.__conf.read(config_path, encoding='utf-8')

    def read_ini(self,src,option):
        return self.__conf.get(src,option)

    @property  #装饰器，可以直接调用方法，不需要加（）
    def url_path(self):
        value = self.read_ini('default','url')
        return value

    @property
    def driver_path(self):
        value = self.read_ini('default','driver_path')
        return value

    @property
    def driver_type(self):
        value = self.read_ini('default','driver_type')
        return value

    @property
    def time_out(self):
        value = float(self.read_ini('default','time_out'))
        return value

    @property
    def screentshot_path(self):
        value = self.read_ini('default', 'screent_shot_path')
        return value

    @property
    def get_default_username(self):
        value = self.read_ini('default', 'username')
        return value

    @property
    def get_default_password(self):
        value = self.read_ini('default', 'password')
        return value

    @property
    def get_log_path(self):
        value = self.read_ini('default', 'log_path')
        return value

    @property
    def get_log_level(self):
        value = self.read_ini('default', 'log_level')
        return int(value)

    @property
    def get_testdata_path(self):
        value = self.read_ini('default', 'test_data_path')
        return value

    @property
    def get_report_path(self):
        value = self.read_ini('default', 'report_path')
        return value

    @property
    def get_case_path(self):
        value = self.read_ini('default', 'case_path')
        return value

Config = ConfigUtils()
if __name__=='__main__':
    current_dir = os.path.dirname(__file__)
    config_utils_obj = Config
    url_path = config_utils_obj.url_path
    now = time.strftime('%Y_%m_%d_H_%M_%S')
    driver_path = Config.screentshot_path
    screentshot_filepath = os.path.join(current_dir, '../UiTtest_%s.png' % now)

    print(Config.get_testdata_path)
