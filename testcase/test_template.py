#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/5 14:25
@Author : 搁浅灬惜缘
@file : test_template.py
'''

import unittest
from business.template import Sina
from base.driver import *
import time
driver = open_browser()
sina = Sina(driver)
class SinaTest(unittest.TestCase):
    def setUp(self):
        sina.maximize_window

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                sina.get_screenshot(case_name)
        time.sleep(2)
        sina.quit()
    def test_login_1(self):
        sina.get_url("https://mail.sina.com.cn")
        sina.login("test","password")
        self.assertEqual("1","2")

if __name__ == '__main__':
    unittest.main(verbosity=2)
