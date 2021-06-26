# encoding:utf-8
# @author:ddx
# @time:2021/6/26 10:49
import unittest
import os
import time
from BeautifulReport import BeautifulReport


current = os.path.dirname(__file__)
report_path = os.path.join(current,'reports')

suite = unittest.defaultTestLoader.discover(start_dir='testcase',
                                            pattern='*_test.py',
                                            top_level_dir='testcase')
main_suite = unittest.TestSuite()
main_suite.addTest(suite)
now = time.strftime('%Y_%m_%d_%H_%M_%S')

filename = 'report'+ now
runner = BeautifulReport(main_suite)
runner.report(filename=filename,description='UI自动化测试',report_dir=report_path,theme='theme_default')
