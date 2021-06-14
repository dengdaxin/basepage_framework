import os
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


Config = ConfigUtils()
if __name__=='__main__':
    config_utils_obj = Config
    url_path = config_utils_obj.url_path
    driver_path = config_utils_obj.driver_path

