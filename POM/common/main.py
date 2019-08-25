#!/usr/bin/python3
# -*-coding:gbk-*-
# @project��python_file
# @author����ľ����
# @file��main.py
# @software��PyCharm
# @time��2019/08/15 11:56:57

from selenium import webdriver
from study_hard.POM.testcase.ExecutionCases import Case


class Wnss:
    # ��������������������
    def __init__(self):
        self.case = Case()

    @classmethod
    def driver(cls):
        # �෽��ֻҪʵ����һ�ξͿ�������
        # cls.dr = webdriver.Chrome()
        cls.dr = webdriver.Firefox()
        cls.dr.get('http://localhost:8080/woniusales/')
        cls.dr.implicitly_wait(3)
        return cls.dr

    def Login(self):
        # ���ǵ��õ�¼�������������
        dr = self.driver()  # ������driver����෽��������Ϳ���ֱ��������.xxֱ�ӵ����������dr�����ˣ���Woniusales.dr ����self.dr
        resul = self.case.case_login(dr)
        if resul == '��¼�ɹ�':
            print('�û���Ϣ��ȷ����¼�ɹ�')
        elif resul == '��¼ʧ��':
            print('�û���Ϣ���󣬵�¼ʧ��')

    def Sale(self):
        # �������۳���
        dr = self.dr
        resul = self.case.case_Sale(dr)
        if resul == '���׳ɹ�':
            print('��Ϣ��ȷ�����׳ɹ�')
        else:
            print('��Ϣ���󣬽���ʧ��')

    def Cancellation(self):
        # ����ע��
        dr = self.dr
        resul = self.case.case_Cancellation(dr)
        if resul == 'ע���ɹ�':
            print('ע���ɹ�')
        elif resul == 'ע��ʧ��':
            print('ע��ʧ��')

    def __del__(self):
        self.dr.close()


def main():
    start = Wnss()
    start.Login()
    start.Sale()
    start.Cancellation()


if __name__ == '__main__':
    main()
