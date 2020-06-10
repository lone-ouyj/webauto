#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/5 14:17
@Author : 搁浅灬惜缘
@file : run_alltest.py
'''

from utils.BSTestRunner import *
from utils.logging_util import Logger
from utils.send_email import Send_Email
import time
import unittest
import os
logging = Logger().get_logger()
def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(base_dir+'/testcase')
    logging.info("获取测试case脚本路径:{0}".format(test_dir))
    nowtime = time.strftime('%Y-%m-%d %H_%M')
    report_name = os.path.join(base_dir+'/report/'+nowtime+'-result.html')
    logging.info("存放报告文件路径:{0}".format(report_name))
    discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
    with open(report_name, 'wb') as f:
        runner = BSTestRunner(stream=f, title="Test Report", description="Test case Result")
        runner.run(discover)
    Logger().close_logger()
    Send_Email()

if __name__=="__main__":
    main()