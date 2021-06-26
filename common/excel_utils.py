# encoding:utf-8
# @author:ddx
# @time:2021/6/24 22:37
import xlrd
import os
from common.config_utils import Config

class ExcelUtils(object):
    def __init__(self,excel_path,sheet_name=None):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.sheet_data = self.__get_sheet_data()

    def __get_sheet_data(self):
        workbook = xlrd.open_workbook(self.excel_path)
        if self.sheet_name:
            sheet = workbook.sheet_by_name(self.sheet_name)
        else:
            sheet = workbook.sheet_by_index(0)
        return sheet

    @property
    def get_row_count(self):
        row_count = self.sheet_data.nrows
        return row_count

    @property
    def get_col_count(self):
        col_count = self.sheet_data.ncols
        return col_count

    def get_sheet_data_by_list(self): #把excel的数据通过列表返回
        all_excel_data = []
        for rownum in range(self.get_row_count):
            row_excel_data = []
            for colnum in range(self.get_col_count):
                cell_value = self.sheet_data.cell_value(rownum,colnum)
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        return all_excel_data

if __name__=='__main__':
    current_path = os.path.dirname(__file__)
    test_data_path = os.path.join(current_path, '..',Config.get_testdata_path)
    excle = ExcelUtils(test_data_path,'login_suite').get_sheet_data_by_list()
    print(excle)