#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/1 14:12
@Author : 搁浅灬惜缘
@file : read_config.py
'''
import configparser
from utils.logging_util import Logger
import os
logging = Logger().get_logger()
class ReadIni():
    def __init__(self,file_name=None):
        self.file_name = file_name
    def loading_config(self):
        '''
        读取ini配位置文件
        :param file_name: ini配置文件路径
        :return:
        '''
        cf = configparser.ConfigParser()
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if self.file_name == None:
            ini_path = os.path.join(base_dir + '/config/' + 'email_config.ini')
        else:
            ini_path = os.path.join(base_dir + '/config/' + self.file_name)
        logging.info("读取配置文件:{0}".format(ini_path))
        cf.read(ini_path,encoding="utf-8-sig")
        return cf

    def get_value(self,node,key):
        result = None
        try:
            cf = self.loading_config()
            result = cf.get(node,key)
            logging.info("成功获取[{0}]下的[{1}]={2}".format(node,key,cf.get(node,key)))
        except:
            logging.error("获取[{0}]下的[{1}]值失败".format(node,key))
        finally:
            Logger().close_logger()
            return result



if __name__ == '__main__':
    # print("./../config/email_config.ini".split(".")[-1])
    t = ReadIni()
    s=t.get_value("email_config","subject")
    print(s)
    print(type(s))