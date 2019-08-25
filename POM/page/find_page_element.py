#!/usr/bin/python3
# -*-coding:gbk-*-
# @project：python_file
# @author：子木仄言
# @file：find_page_element.py
# @software：PyCharm
# @time：2019/08/15 12:03:15

class Find_page_elment:
    # 这是查找页面元素的模块
    def login_element(self, dr):
        # 这是查找登录页面元素的方法
        user = dr.find_element_by_id('username')  # 用户框元素
        pwd = dr.find_element_by_id('password')  # 密码框元素
        code = dr.find_element_by_id('verifycode')  # 验证码框元素
        button = dr.find_element_by_xpath('/html/body/div[4]/div/form/div[6]/button')  # 登录按钮元素
        # Success = dr.find_element_by_link_text('注销')                      #登录成功之后找到注销的元素
        # fail = dr.find_element_by_link_text('尚未登录')                     #登录失败找的页面元素
        return user, pwd, code, button

    def Sale_element(self, dr):
        # 以下都是查找销售出库页面元素的方法
        return dr.find_element_by_xpath('//*[@id="navbar"]/ul[1]/li[1]/a')  # 销售出库导航栏

    def Sale_element_Barcode_Text(self, dr):
        return dr.find_element_by_id('barcode')

    def Sale_element_Barcode_button(self, dr):
        return dr.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]/form/button')  # 条形码旁边的确认按钮

    def Sale_element_phone_text(self, dr):
        return dr.find_element_by_id('customerphone')  # 输入会员电话文本框

    def Sale_element_msg(self, dr):
        return dr.find_element_by_xpath('//*[@id="vipsell"]/div[1]/form/div[2]/button')  # 查询会员信息

    def Sale_element_Receivables(self, dr):
        return dr.find_element_by_id('submit')  # 确认收款

    def Cancellation_element_(self,dr):
        return dr.find_element_by_xpath('//*[@id="navbar"]/ul[2]/li[2]/a')