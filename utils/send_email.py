#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/4 21:05
@Author : 搁浅灬惜缘
@file : send_email.py
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
from utils.ini_util import ReadIni
from utils.logging_util import Logger
import os
import time
read_ini = ReadIni("email_config.ini")
logging = Logger().get_logger()
class Send_Email():
    def __init__(self):
        self.annex = read_ini.get_value("email_config","annex")
        self.smtpserver = read_ini.get_value("email_config","smtpserver")
        self.sender = read_ini.get_value("email_config","sender")
        self.password = read_ini.get_value("email_config","password")
        self.split = read_ini.get_value("email_config","split")
        self.receives = read_ini.get_value("email_config","receives").split(self.split)
        self.subject = time.strftime("%Y-%m-%d")+read_ini.get_value("email_config","subject")
        self.content = read_ini.get_value("email_config","content")
        if self.annex == "1":
            logging.info("邮件包含附件")
            self.send_email_anner()
        else:
            logging.info("邮件不包含附件")
            self.send_email_noanner()
        Logger().close_logger()

    def send_email_noanner(self):
        try:
            msg = MIMEText(self.content, 'html', 'utf-8')
            msg['Subject'] = Header(self.subject, 'utf-8')
            msg['From'] = self.sender
            msg['To'] = ';'.join(self.receives)

            smtp = smtplib.SMTP_SSL(self.smtpserver, 465)
            logging.info("连接邮件服务器")
            smtp.helo(self.smtpserver)
            smtp.ehlo(self.smtpserver)
            smtp.login(self.sender, self.password)
            logging.info("登录邮件服务器")

            smtp.sendmail(self.sender, self.receives, msg.as_string())
            logging.info("发送邮件成功")
            smtp.quit()
        except:
            logging.error("发送邮件失败")
        finally:
            Logger().close_logger()


    def send_email_anner(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        report_dir = os.path.join(base_dir+"/report")
        report_html = sorted(os.listdir(report_dir),key=lambda x:os.path.getatime(report_dir+"/"+x),reverse=True)[0]
        file_dir = os.path.join(report_dir+'/'+report_html)
        logging.info("获取最新的测试报告文件:{0}".format(file_dir))

        try:
            msgRoot = MIMEMultipart()
            msgRoot['Subject'] = self.subject
            msgRoot['From'] = self.sender
            msgRoot['To'] = ';'.join(self.receives)
            msgRoot.attach(MIMEText(self.content, 'html', 'utf-8'))

            # att = MIMEApplication(open(file_dir, "rb").read())
            # att.add_header("Content-Disposition","attachment",file_name=report_html)
            # msgRoot.attach(att)
            att = MIMEText(open(file_dir,'rb').read(),'base64','utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename={0}'.format(report_html)
            msgRoot.attach(att)
            logging.info("添加附件:{0}".format(report_html))

            smtp = smtplib.SMTP_SSL(self.smtpserver, 465)
            smtp.helo(self.smtpserver)
            smtp.ehlo(self.smtpserver)
            smtp.login(self.sender, self.password)
            logging.info("登录邮件服务器")

            smtp.sendmail(self.sender, self.receives, msgRoot.as_string())
            logging.info("发送邮件成功")
            smtp.quit()
        except:
            logging.error("发送邮件失败")
        finally:
            Logger().close_logger()

if __name__ == '__main__':
    t = Send_Email()