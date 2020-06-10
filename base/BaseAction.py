#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/3 21:40
@Author : 搁浅灬惜缘
@file : Base.py
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from utils.logging_util import Logger
# from PIL import Image, ImageEnhance
# import pytesseract
from utils.ini_util import ReadIni
from base.driver import *
import os
import time
logging = Logger().get_logger()
sys_default = ReadIni("sys_config.ini")

class WebDriver():
    def __init__(self,driver):
        self.timeout = int(sys_default.get_value("sys_default","timeout"))
        self.driver = driver
        # self.driver = open_browser()

    def get_url(self,url):
        logging.info("访问url:{0}".format(url))
        self.driver.get(url)
        Logger().close_logger()

    def find_element(self, *loc):
        '''
        单个元素定位方法
        :param loc: 定位元素信息
        :return: 返回定位的元素信息，否则不返回
        '''
        logging.info("定位元素{0}开始".format(loc))
        element = None
        try:
            element = WebDriverWait(self.driver,self.timeout).until(lambda x:x.find_element(*loc))
            logging.info("已定位到元素")
        except:
            logging.error("未定位到元素{0}".format(loc))
        finally:
            logging.info("定位元素{0}结束".format(loc))
        Logger().close_logger()
        return element

    def find_elements(self, *loc):
        '''
        一组元素定位方法
        :param loc: 定位元素信息
        :return: 返回定位的元素组信息，否则不返回
        '''
        logging.info("定位元素{0}开始".format(loc))
        element = None
        try:
            element = WebDriverWait(self.driver,self.timeout).until(lambda x:x.find_elements(*loc))
            logging.info("已定位到元素")
        except:
            logging.error("未定位到元素{0}".format(loc))
        finally:
            logging.info("定位元素{0}结束".format(loc))
            Logger().close_logger()
            return element

    def input_value(self, loc, value):
        '''
        在输入框中输入值
        :param value: 输入值
        :param loc: 定位元素信息
        :return: 无
        '''
        element = self.find_element(*loc)
        if element:
            logging.info("输入值:{0}".format(value))
            element.send_keys(value)
        else:
           logging.error("无法输入值")
        Logger().close_logger()

    def click_element(self, *loc):
        '''
        点击元素
        :param loc: 定位元素信息
        :return: 无
        '''
        element = self.find_element(*loc)
        if element:
            logging.info("点击元素:{0}".format(loc))
            element.click()
        else:
            logging.error("无法点击元素")
        Logger().close_logger()

    def clear_element(self, *loc):
        '''
        清空输入框
        :param loc: 定位元素信息
        :return: 无
        '''
        element = self.find_element(*loc)
        if element:
            logging.info("清空输入框:{0}".format(loc))
            element.clear()
        else:
            logging.error("无法清空输入框")
        Logger().close_logger()

    def get_cookie(self):
        '''
        获取页面cookie信息
        :return:返回cookies
        '''
        logging.info("获取cookie信息：{0}".format(self.driver.get_cookies()))
        Logger().close_logger()
        return  self.driver.get_cookies()

    def add_cookie(self, **kwargs):
        '''
        添加cookie信息，以字典方式传入
        :param kwargs: 要添加的cookie信息
        :return:
        '''
        logging.info("添加cookie:{0}".format(kwargs))
        self.driver.add_cookie(kwargs)
        Logger().close_logger()

    def del_cookie(self, name):
        '''
        删除cookie信息，传入cookie名称即可
        :param kwargs: 要删除的cookie信息
        :return:
        '''
        logging.info("删除cookie:{0}".format(name))
        self.driver.delete_cookie(name)
        Logger().close_logger()

    def get_screenshot(self, screenshotname):
        '''
        获取页面截图，传入截图名称，无需后缀
        :param screenshotname: 截图名称
        :return:
        '''
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        picture_dir = os.path.join(base_dir+'\\screenshot\\'+str(screenshotname)+'.png')
        logging.info("截图保存位置:{0}".format(picture_dir))
        self.driver.save_screenshot(picture_dir)
        Logger().close_logger()
        return picture_dir

    @property
    def maximize_window(self):
        '''
        窗口最大化
        :return:
        '''
        logging.info("窗口最大化")
        self.driver.maximize_window()
        Logger().close_logger()

    def set_window_size(self, width, height):
        '''
        设置窗口大小
        :param width: 宽
        :param height: 高
        :return:
        '''
        logging.info("设置窗口宽:{0} 高:{1}".format(width, height))
        self.driver.set_window_size(width, height)
        Logger().close_logger()

    def get_window_size(self):
        '''
        获取窗口大小
        :return:
        '''
        logging.info("窗口宽为:{0} 高为:{1}".format(self.driver.get_window_size()['width'],self.driver.get_window_size()['height']))
        size = self.driver.get_window_size()
        Logger().close_logger()
        return size

    @property
    def refresh_window(self):
        '''
        刷新窗口
        :return:
        '''
        logging.info("刷新窗口")
        self.driver.refresh()
        Logger().close_logger()

    @property
    def forward_window(self):
        '''
        浏览器前进
        :return:
        '''
        logging.info("页面前进")
        self.driver.forward()
        Logger().close_logger()

    @property
    def back_window(self):
        '''
        浏览器后退
        :return:
        '''
        logging.info("页面后退")
        self.driver.back()
        Logger().close_logger()

    def get_element_size(self,*loc):
        '''
        获取元素尺寸
        :param loc: 定位元素信息
        :return: 元素尺寸，失败返回None
        '''
        element = self.find_element(*loc)
        if element:
            logging.info("获取元素尺寸:{0}".format(element.size))
            element_size = element.size
        else:
            logging.error("无法获取元素尺寸")
            element_size = None
        Logger().close_logger()
        return element_size

    def get_element_text(self,*loc):
        '''
        获取元素文本信息
        :param loc: 定位元素信息
        :return: 元素文本，失败返回None
        '''
        element = self.find_element(*loc)
        if element:
            logging.info("获取元素文本信息:{0}".format(element.text))
            element_text = element.text
        else:
            logging.error("无法获取元素文本信息")
            element_text = None
        Logger().close_logger()
        return element_text

    def get_element_attribute(self, loc, type):
        '''
        获取元素属性值
        :param loc:定位元素信息
        :return:属性值，失败返回None
        '''
        element = self.find_element(*loc)
        if element:
            logging.info("元素属性值:{0}".format(element.get_attribute(type)))
            element_attribute = element.get_attribute(type)
        else:
            logging.error("无法获取元素属性值")
            element_attribute = None
        Logger().close_logger()
        return element_attribute

    def get_location(self,*loc):
        '''
        获取元素坐标
        :param loc: 定位元素信息
        :return:元素坐标
        '''
        element = self.find_element(*loc)
        if element:
            logging.info("元素坐标信息:{0}".format(element.location))
            element_location = element.location
        else:
            logging.error("无法获取元素坐标信息")
            element_location = None
        Logger().close_logger()
        return element_location

    def get_is_selected(self,*loc):
        '''
        获取元素是否已选中
        :param loc: 定位元素信息
        :return: 返回True or False or None
        '''
        element = self.find_element(*loc)
        if element:
            if element.is_selected() == True:
                logging.logger.info("元素已选中")
                element_selected = True
            else:
                logging.info("元素未选中")
                element_selected = False
        else:
            logging.error("无法获取元素选中状态")
            element_selected = None
        Logger().close_logger()
        return element_selected

    def get_is_enabled(self,*loc):
        '''
        获取元素是否可编辑
        :param loc: 定位元素信息
        :return: 返回True or False or None
        '''
        element = self.find_element(*loc)
        if element:
            if element.is_enabled() == True:
                logging.info("元素可编辑")
                element_selected = True
            else:
                logging.info("元素不可编辑")
                element_selected = False
        else:
            logging.error("无法获取元素编辑状态")
            element_selected = None
        Logger().close_logger()
        return element_selected

    @property
    def get_title(self):
        '''
        获取页面title
        :return:
        '''
        logging.info("页面title信息:{0}".format(self.driver.title))
        Logger().close_logger()
        return self.driver.title

    @property
    def get_current_url(self):
        '''
        获取页面url地址
        :return:
        '''
        logging.info("页面url地址:{0}".format(self.driver.current_url))
        Logger().close_logger()
        return self.driver.current_url

    @property
    def get_driver_name(self):
        logging.info("浏览器名称:{0}".format(self.driver.name))
        Logger().close_logger()
        return self.driver.name
    @property
    def get_page_source(self):
        logging.info("页面源码:{0}".format(self.driver.page_source))
        Logger().close_logger()
        return self.driver.page_source

    def switch_iframe(self,name):
        '''
        切换iframe窗口
        :param name: iframe窗口id
        :return:
        '''
        logging.info("切换iframe:{0}".format(self.driver.switch_to.frame(name)))
        Logger().close_logger()
        return self.driver.switch_to.frame(name)

    @property
    def switch_dafult_iframe(self):
        '''
        返回主iframe窗口
        :return:
        '''
        logging.info("切换主iframe窗口")
        self.driver.switch_to_default_content()
        Logger().close_logger()

    @property
    def switch_parent_iframe(self):
        '''
        返回到父iframe窗口
        :return:
        '''
        logging.info("切换父iframe窗口")
        self.driver.switch_to.parent_frame()
        Logger().close_logger()
    @property
    def alert_accept(self):
        '''
        获取alert并点击确定按钮
        :return:
        '''
        try:
            accept = self.driver.switch_to.alert()
            logging.info("获取alert并点击确定")
            accept.accept()
        except:
            logging.error("未获取到alert")
        finally:
            Logger().close_logger()

    @property
    def alert_dismiss(self):
        '''
        获取alert并点击取消按钮
        :return:
        '''
        try:
            accept = self.driver.switch_to.alert()
            logging.info("获取alert并点击取消")
            accept.dismiss()
        except:
            logging.error("未获取到alert")
        finally:
            Logger().close_logger()

    def alert_send_keys(self,value):
        try:
            accept = self.driver.switch_to.alert()
            logging.info("获取alert并输入值")
            accept.send_keys(value)
        except:
            logging.error("未获取到alert")
        finally:
            Logger().close_logger()

    def mouse_right_click(self, *loc):
        '''
        鼠标右击定位的元素
        :param loc: 定位元素信息
        :return:
        '''
        element = self.find_element(*loc)
        if element:
            logging.info("右击")
            ActionChains(self.driver).context_click(element).perform()
        else:
            logging.error("无法右击")
        Logger().close_logger()

    def mouse_double_click(self, *loc):
        '''
        鼠标双击定位的元素
        :param loc: 定位元素信息
        :return:
        '''
        element = self.find_element(*loc)
        if element:
            logging.info("双击元素:{0}".format(loc))
            ActionChains(self.driver).double_click(element).perform()
        else:
            logging.error("无法双击")
        Logger().close_logger()

    def mouse_drag_drop(self, loc, target):
        '''
        从loc拖动到target位置
        :param loc:
        :param target:
        :return:
        '''
        element = self.find_element(*loc)
        goal = self.find_element(*target)
        if element and goal:
            ActionChains(self.driver).drag_and_drop(element, goal).perform()
            logging.info("从{0}拖动到{1}".format(loc, target))
        else:
            logging.error("无法拖动")
        Logger().close_logger()

    def mouse_move(self, *loc):
        '''
        鼠标悬停
        :param loc: 定位元素信息
        :return:
        '''
        element = self.find_element(*loc)
        if element:
            ActionChains(self.driver).move_to_element(element).perform()
            logging.info("鼠标悬停在元素:{0}上".format(loc))
        else:
            logging.error("鼠标无法悬停在元素上")
        Logger().close_logger()

    def mouse_left_click(self,*loc):
        element = self.find_element(*loc)
        if element:
            ActionChains(self.driver).click(element).perform()
            logging.info("鼠标点击元素:{0}".format(loc))
        else:
            logging.error("鼠标无法点击元素")
        Logger().close_logger()

    def mouse_move_offset(self,x,y):
        '''移动鼠标到x,y位置'''
        logging.info("鼠标移动到[{0},{1}]位置".format(x,y))
        Logger().close_logger()
        return ActionChains(self.driver).move_by_offset(x,y)

    def mouse_drag_drop_offset(self,loc,x,y):
        '''
        拖拽元素到指定位置
        :param loc: 定位元素信息
        :param x: x坐标
        :param y: y坐标
        :return:
        '''
        element = self.find_element(*loc)
        if element:
            ActionChains(self.driver).drag_and_drop_by_offset(element, x, y)
            logging.info("将元素:{0}拖拽到[{1},{2}]".format(loc,x,y))
        else:
            logging.error("无法拖拽元素到指定位置")
        Logger().close_logger()

    def select_index(self, loc, index):
        '''
        下拉选择下标index项，从0开始
        :param index:下标
        :param loc:定位元素信息
        :return:
        '''
        element = self.find_element(*loc)
        try:
            Select(element).select_by_index(index)
            logging.info("下拉选择index={0}".format(index))
        except:
            logging.error("无法下拉选择")
        finally:
            Logger().close_logger()

    def select_visible_text(self, loc, text):
        '''
        下拉选择显示的text文本信息
        :param text:文本信息
        :param loc:定位元素信息
        :return:
        '''
        element = self.find_element(*loc)
        try:
            Select(element).select_by_visible_text(text)
            logging.info("下拉选择text={0}".format(text))
        except:
            logging.error("无法下拉选择")
        finally:
            Logger().close_logger()

    def select_value(self,loc, value):
        '''
        下拉选择对应的value项
        :param value:
        :param loc: 定位元素信息
        :return:
        '''
        element = self.find_element(*loc)
        try:
            Select(element).select_by_value(value)
            logging.info("下拉选择value={0}".format(value))
        except:
            logging.error("无法下拉选择")
        finally:
            Logger().close_logger()

    def execute_script(self, script, *args):
        '''
        执行js脚本
        :param script: js脚本
        :param args:
        :return:
        '''
        data = None
        try:
            data = self.driver.execute_script(script, *args)
            logging.info("执行script脚本:{0}-{1}".format(script, args))
        except:
            logging.error("无法执行script脚本")
        finally:
            Logger().close_logger()
            return data

    def js_scroll_top(self):
        '''
        滑动到页面顶部
        :return:
        '''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
        logging.info("滑动到页面顶部")
        Logger().close_logger()

    def js_scroll_end(self):
        '''
        滑动到页面底部
        :return:
        '''
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)
        logging.info("滑动到页面底部")
        Logger().close_logger()
    # def failed_screeshot(self):
    #     '''
    #     用例失败后自动截图
    #     :return:
    #     '''
    #     for method_name, error in self._outcome.errors:
    #         if error:
    #             case_name = self._testMethodName
    #             self.get_screenshot(case_name)
    #             logging.info("用例执行失败，截图名称:{0}".format(case_name+'png'))
    #     Logger().close_logger()
    # def get_verify_code(self, loc, screenshot="verifyCode"):
    #     '''获取图片验证码'''
    #     screenImg = self.get_screenshot(screenshot)
    #     location = self.get_location(*loc)
    #     size = self.get_element_size(*loc)
    #
    #     left = location['x']
    #     top = location['y']
    #     right = location['x'] + size['width']
    #     bottom = location['y'] + size['height']
    #
    #     im = Image.open(screenImg)
    #     img = im.crop((left, top, right, bottom))
    #     img.convert('L')  # 转换模式：L|RGB
    #     img = ImageEnhance.Contrast(img)  # 增加对比度
    #     img = img.enhance(2.0)  # 增加饱和度
    #     img.save(screenImg)

        # 再次读取验证码
        # img = Image.open(screenImg)
        # time.sleep(1)
        # code = pytesseract.image_to_string(img)
        # return code

    def close(self):
        logging.info("关闭窗口")
        self.driver.close()
        Logger().close_logger()

    def quit(self):
        logging.info("关闭浏览器")
        self.driver.quit()
        Logger().close_logger()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    t = WebDriver(driver)
    t.maximize_window
    t.driver.get("http://mail.sina.com.cn")
    loc = (By.ID, 'freename')
    # t.input_value(loc, "test")
    cookies = {"name":"test","value":"123456"}
    t.get_element_attribute(loc,"type")
    time.sleep(5)
    t.quit()



