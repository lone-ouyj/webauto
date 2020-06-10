#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/3 21:34
@Author : 搁浅灬惜缘
@file : logging_util.py
'''
import logging
import os
import time

class Logger():
    def __init__(self,levelno=logging.INFO):
        self.logger = logging.getLogger()
        self.logger.setLevel(levelno)
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.log_name = os.path.join(self.base_dir + '/log/' + time.strftime("%Y-%m-%d") + '.log')
        self.file_handle = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        self.file_handle.setFormatter(
            logging.Formatter('%(asctime)s %(filename)s-->%(funcName)s [line:%(lineno)d] [%(levelname)s]:%(message)s'))

    def get_logger(self):
        if not self.logger.handlers:
            self.logger.addHandler(self.file_handle)
        return self.logger

    def close_logger(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == '__main__':
    logger = Logger().get_logger()
    logger.info("tex1t")
    Logger().close_logger()
