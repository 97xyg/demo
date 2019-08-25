#!/usr/bin/python3
# -*-coding:gbk-*-
# @project：python_file
# @author：子木仄言
# @file：ExecutionCases.py
# @software：PyCharm
# @time：2019/08/15 12:12:29
import time

from study_hard.POM.page.find_page_element import Find_page_elment


class Case:
    # 这是执行用例的模块
    def __init__(self):
        self.get_element = Find_page_elment()

    def case_login(self, dr):
        # 这是登录的用例脚本
        user, pwd, code, button = self.get_element.login_element(dr)
        user.send_keys('admin')
        pwd.send_keys('admin')
        code.send_keys('0000')
        button.click()
        try:
            dr.find_element_by_link_text('注销').text == '注销'
            return '登录成功'
        except:
            dr.find_element_by_link_text('尚未登录').text == '尚未登录'
            return '登录失败'

    def case_Sale(self, dr):
        # 这是执行销售出库模块的用例的方法
        self.get_element.Sale_element(dr).click()
        self.get_element.Sale_element_Barcode_Text(dr).send_keys('6955203644985')
        self.get_element.Sale_element_Barcode_button(dr).click()
        self.get_element.Sale_element_phone_text(dr).send_keys('18682558655')
        self.get_element.Sale_element_msg(dr).click()
        self.get_element.Sale_element_Receivables(dr).click()
        try:
            if '请确认你已经真实收到' in dr.switch_to.alert.text:
                dr.switch_to.alert.accept()
                return '交易成功'
        except:
            return '交易失败'

    def case_Cancellation(self,dr):
        #这是执行注销的用例
        self.get_element.Cancellation_element_(dr).click()
        try:
            dr.find_element_by_link_text('注销').text == '注销'
            return '注销失败'
        except:
            dr.find_element_by_link_text('尚未登录').text == '尚未登录'
            return '注销成功'