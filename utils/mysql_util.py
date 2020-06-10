#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/16 22:42
@Author : 搁浅灬惜缘
@file : mysql_util.py
'''
import pymysql
from utils.ini_util import ReadIni
from utils.logging_util import Logger

read_ini = ReadIni("mysql_config.ini")
logging = Logger().get_logger()

localhost = read_ini.get_value("mysql","localhost")
port = int(read_ini.get_value("mysql","port"))
user = read_ini.get_value("mysql","user")
password = read_ini.get_value("mysql","password")
databasename = read_ini.get_value("mysql","databasename")
def connect_mysql():
    db = pymysql.connect(host=localhost,
                         user=user,
                         port=port,
                         password=password,
                         db=databasename,
                         charset="utf8")
    cursor = db.cursor()
    sql = "select * from ap_t_label"
    cursor.execute(sql)
    print(cursor.fetchone())
    cursor.close()
    db.close()

connect_mysql()