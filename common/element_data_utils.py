import os
import xlrd
from common.config_utils import Config

current = os.path.dirname(__file__)
excel_path = os.path.join(current,'../element_info_datas/element_infos.xlsx')

class ElementdataUtils:
    def __init__(self,module_name,page_name,excel_path=excel_path):
        self.excel_path = excel_path
        self.workbook = xlrd.open_workbook(excel_path)
        self.sheet = self.workbook.sheet_by_name(module_name)
        self.row_count = self.sheet.nrows
        self.page_name = page_name
    def get_element_info(self):
        element_infos = {}
        for i in range(1, self.row_count):
            if self.sheet.cell_value(i,2) == self.page_name:
                element_info = {}
                element_info['element_name'] = self.sheet.cell_value(i, 1)
                element_info['locator_type'] = self.sheet.cell_value(i, 3)
                element_info['locator_value'] = self.sheet.cell_value(i, 4)
                '''如果excel没设置时间，或者设置的时间不是浮点型，都将结果强制为默认值5'''
                element_info['timeout'] = self.sheet.cell_value(i, 5) if isinstance(self.sheet.cell_value(i, 5),float) else Config.time_out
                element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos

if __name__=='__main__':
    element = ElementdataUtils('login','login_page').get_element_info()
    for i,j in element.items():
        print(i,j)