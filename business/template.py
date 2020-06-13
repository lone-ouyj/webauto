#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/3 21:32
@Author : 搁浅灬惜缘
@file : template.py
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.BaseAction import WebDriver
from utils.logging_util import Logger
import time
logging = Logger().get_logger()
class Sina(WebDriver):
    username_loc = (By.ID,'freename')
    password_loc = (By.ID,'freepassword')
    login_loc = (By.LINK_TEXT,'登录')

    def login(self,username,password):
        self.input_value(self.username_loc,username)
        logging.info("用户名:{0}".format(username))
        self.input_value(self.password_loc, password)
        logging.info("密码:{0}".format(password))
        self.click_element(self.login_loc)
        logging.info("点击登录按钮")
        Logger().close_logger()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    t = Sina(driver)
    t.get_url("https://mail.sina.com.cn")
    t.login("test","password")
    time.sleep(2)
    t.quit()

