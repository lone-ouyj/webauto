# python+selenium+unittest+BSTestRunner框架介绍
###### **1.环境准备**
python版本：python3.8

selenium版本：selenium3.141.0 [使用python自带的pip命令安装即可，下同]

ddt版本：ddt1.4.1

pymysql版本：pymysql0.9.3

xlrd版本：xlrd1.2.0

###### **2.项目介绍**
base中存放封装好的selenium方法BaseAction.py和启动浏览器的类型driver.py;

business中存放各个业务模块的封装

config中存放一些配置文件

data中可存放测试用例

log中存放运行的日志，自动生成

report中存放运行测试用例的报告结果，通过BSTestRunner生成

screenshot中存放运行中的截图

testcase中存放各个业务模块的用例

utils中存放日志收集、邮件信息、excel操作、msyql数据库操作、获取配置信息等功能类和方法

run_alltest.py运行testcase中所有的用例集

###### **3.后期工作**
1.完善对mysql数据库的操作

2.增加对excel文件的写入操作