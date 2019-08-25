#!/usr/bin/python3
# -*-coding:gbk-*-
# @project��python_file
# @author����ľ����
# @file��ExecutionCases.py
# @software��PyCharm
# @time��2019/08/15 12:12:29
import time

from study_hard.POM.page.find_page_element import Find_page_elment


class Case:
    # ����ִ��������ģ��
    def __init__(self):
        self.get_element = Find_page_elment()

    def case_login(self, dr):
        # ���ǵ�¼�������ű�
        user, pwd, code, button = self.get_element.login_element(dr)
        user.send_keys('admin')
        pwd.send_keys('admin')
        code.send_keys('0000')
        button.click()
        try:
            dr.find_element_by_link_text('ע��').text == 'ע��'
            return '��¼�ɹ�'
        except:
            dr.find_element_by_link_text('��δ��¼').text == '��δ��¼'
            return '��¼ʧ��'

    def case_Sale(self, dr):
        # ����ִ�����۳���ģ��������ķ���
        self.get_element.Sale_element(dr).click()
        self.get_element.Sale_element_Barcode_Text(dr).send_keys('6955203644985')
        self.get_element.Sale_element_Barcode_button(dr).click()
        self.get_element.Sale_element_phone_text(dr).send_keys('18682558655')
        self.get_element.Sale_element_msg(dr).click()
        self.get_element.Sale_element_Receivables(dr).click()
        try:
            if '��ȷ�����Ѿ���ʵ�յ�' in dr.switch_to.alert.text:
                dr.switch_to.alert.accept()
                return '���׳ɹ�'
        except:
            return '����ʧ��'

    def case_Cancellation(self,dr):
        #����ִ��ע��������
        self.get_element.Cancellation_element_(dr).click()
        try:
            dr.find_element_by_link_text('ע��').text == 'ע��'
            return 'ע��ʧ��'
        except:
            dr.find_element_by_link_text('��δ��¼').text == '��δ��¼'
            return 'ע���ɹ�'