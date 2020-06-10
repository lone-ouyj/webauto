#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/3 21:32
@Author : 搁浅灬惜缘
@file : driver.py
'''
from selenium import webdriver
from utils.logging_util import Logger
logging = Logger().get_logger()
def open_browser(browertype="Chrome"):
    if "Chrome" in browertype:
        logging.info("启动Chrome浏览器")
        driver = webdriver.Chrome()
    elif "firefox" in browertype:
        logging.info("启动Firefox浏览器")
        driver = webdriver.Firefox()
    elif "ie" in browertype:
        logging.info("启动Ie浏览器")
        driver = webdriver.Ie()
    elif "PhantomJS" in browertype:
        logging.info("启动PhantomJS浏览器")
        driver = webdriver.PhantomJS()
    else:
        logging.info("启动默认Chrome浏览器")
        driver = webdriver.Chrome()
    Logger().close_logger()
    return driver

if __name__ == '__main__':
    t = open_browser("PhantomJS")
