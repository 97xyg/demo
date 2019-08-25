#!/usr/bin/python3
# -*-coding:gbk-*-
# @project：python_file
# @author：子木仄言
# @file：main.py
# @software：PyCharm
# @time：2019/08/15 11:56:57

from selenium import webdriver
from study_hard.POM.testcase.ExecutionCases import Case


class Wnss:
    # 这是主函数，程序的入口
    def __init__(self):
        self.case = Case()

    @classmethod
    def driver(cls):
        # 类方法只要实例化一次就可以用了
        # cls.dr = webdriver.Chrome()
        cls.dr = webdriver.Firefox()
        cls.dr.get('http://localhost:8080/woniusales/')
        cls.dr.implicitly_wait(3)
        return cls.dr

    def Login(self):
        # 这是调用登录测试用例的入口
        dr = self.driver()  # 调用了driver这个类方法，后面就可以直接用类名.xx直接调用他里面的dr驱动了，如Woniusales.dr 或者self.dr
        resul = self.case.case_login(dr)
        if resul == '登录成功':
            print('用户信息正确，登录成功')
        elif resul == '登录失败':
            print('用户信息错误，登录失败')

    def Sale(self):
        # 这是销售出库
        dr = self.dr
        resul = self.case.case_Sale(dr)
        if resul == '交易成功':
            print('信息正确，交易成功')
        else:
            print('信息错误，交易失败')

    def Cancellation(self):
        # 这是注销
        dr = self.dr
        resul = self.case.case_Cancellation(dr)
        if resul == '注销成功':
            print('注销成功')
        elif resul == '注销失败':
            print('注销失败')

    def __del__(self):
        self.dr.close()


def main():
    start = Wnss()
    start.Login()
    start.Sale()
    start.Cancellation()


if __name__ == '__main__':
    main()
