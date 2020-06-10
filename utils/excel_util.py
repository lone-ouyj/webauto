#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/3 21:34
@Author : 搁浅灬惜缘
@file : excel_util.py
'''

import xlrd
import os
from utils.logging_util import Logger
logging = Logger().get_logger()
class ExceUtil():
    def __init__(self,excel_file=None,index=None):
        '''
        需传入文件名称和sheet表格，默认为0
        '''
        self.excel_file = excel_file
        self.index = index

    def get_file(self):
        '''
        获取文件完整路径
        :return:
        '''
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if self.excel_file == None:
            excel_path = os.path.join(base_dir + '/data/' + 'template.xls')
        else:
            excel_path = os.path.join(base_dir + '/data/' + self.excel_file)
        if self.index == None:
            self.index = 0
        try:
            logging.info("获取Excel文件:{0}".format(excel_path))
            self.data = xlrd.open_workbook(excel_path)
            logging.info("获取Excel的第{0}个sheet".format(self.index + 1))
            self.table = self.data.sheets()[self.index]
        except:
            logging.error("获取Excel文件失败")

    def get_data(self):
        '''
        获取文件数据内容
        :return:
        '''
        result = []
        self.get_file()
        try:
            logging.info("获取Excel的总行数:{0}".format(self.table.nrows))
            for i in range(self.table.nrows):
                logging.info("获取第{0}行数据:{1}".format(i+1,self.table.row_values(i)))
                col = self.table.row_values(i)
                result.append(col)
        except:
            logging.error("获取Excel文件内容失败")
        Logger().close_logger()
        return result

    def get_lines(self):
        '''
        获取Excel文件总行数
        :return:
        '''
        self.get_file()
        row = None
        try:
            logging.info("获取Excel总行数:{0}".format(self.table.nrows))
            row = self.table.nrows
        except:
            logging.error("获取Excel总行数失败")
        Logger().close_logger()
        return row

    def get_cols(self):
        self.get_file()
        col = None
        try:
            logging.info("获取Excel总列数:{0}".format(self.table.ncols))
            col = self.table.ncols
        except:
            logging.error("获取Excel总列数失败")
        Logger().close_logger()
        return col

    def get_col_value(self,row,col):
        '''
        获取单元格的值
        :param row: 行号
        :param col: 列号
        :return: 单元格值
        '''
        self.get_file()
        data = None
        try:
            logging.info("获取Excel第{0}行第{1}列的值:{2}".format(row,col,self.table.cell(row-1,col-1).value))
            data = self.table.cell(row-1,col-1).value
        except:
            logging.error("获取Excel单元格值失败")
        Logger().close_logger()
        return data

if __name__ == '__main__':
    x = ExceUtil()
    print(x.get_col_value(3,2))