#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/5 12:52
@Author : 搁浅灬惜缘
@file : xml_util.py
'''
import os
from xml.dom import minidom
from utils.logging_util import Logger
logging = Logger().get_logger()
class Xml():
    def __init__(self,filename=None):
        if filename == None:
            self.filename = "template.xml"
        else:
            self.filename = filename
        logging.info("文件名称:{0}".format(self.filename))

    def dir_base(self):
        '''
        获取data文件夹下的文件
        :param filename:要读取的文件名称
        '''
        file_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/data/'+self.filename)
        logging.info("文件路径:{0}".format(file_dir))
        return file_dir

    def getXmlDate(self, node):
        '''
        获取xml文件节点中数据
        :param value:xml 文件夹中单节点名称
        '''
        data = None
        try:
            dom = minidom.parse(self.dir_base())
            db = dom.documentElement
            name = db.getElementsByTagName(node)
            data = name[0].firstChild.data
            logging.info("获取节点数据:{0}".format(data))
        except:
            logging.error("无法获取节点数据")
        finally:
            Logger().close_logger()
        return data

    def getXmlUser(self,node,name):
        '''
        获取节点中属性值
        :param node: xml文件中节点名称
        :param name: xml文件中属性名称
        :return:
        '''
        data = None
        try:
            dom = minidom.parse(self.dir_base())
            db = dom.documentElement
            itemlist = db.getElementsByTagName(node)
            item = itemlist[0]
            if item.getAttribute(name):
                data = item.getAttribute(name)
                logging.info("获取节点[{0}]下[{1}]的属性值:{2}".format(node, name, data))
            else:
                data = None
                logging.info("无法获取节点下的属性值")
        except:
            logging.error("无法获取节点")
        finally:
            Logger().close_logger()
        return data

if __name__ == '__main__':
    t = Xml("template.xml")
    print(t.getXmlUser('driverText','emailNull'))