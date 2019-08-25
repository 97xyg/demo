#!/usr/bin/python3
# -*-coding:gbk-*-
# @project��python_file
# @author����ľ����
# @file��find_page_element.py
# @software��PyCharm
# @time��2019/08/15 12:03:15

class Find_page_elment:
    # ���ǲ���ҳ��Ԫ�ص�ģ��
    def login_element(self, dr):
        # ���ǲ��ҵ�¼ҳ��Ԫ�صķ���
        user = dr.find_element_by_id('username')  # �û���Ԫ��
        pwd = dr.find_element_by_id('password')  # �����Ԫ��
        code = dr.find_element_by_id('verifycode')  # ��֤���Ԫ��
        button = dr.find_element_by_xpath('/html/body/div[4]/div/form/div[6]/button')  # ��¼��ťԪ��
        # Success = dr.find_element_by_link_text('ע��')                      #��¼�ɹ�֮���ҵ�ע����Ԫ��
        # fail = dr.find_element_by_link_text('��δ��¼')                     #��¼ʧ���ҵ�ҳ��Ԫ��
        return user, pwd, code, button

    def Sale_element(self, dr):
        # ���¶��ǲ������۳���ҳ��Ԫ�صķ���
        return dr.find_element_by_xpath('//*[@id="navbar"]/ul[1]/li[1]/a')  # ���۳��⵼����

    def Sale_element_Barcode_Text(self, dr):
        return dr.find_element_by_id('barcode')

    def Sale_element_Barcode_button(self, dr):
        return dr.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]/form/button')  # �������Աߵ�ȷ�ϰ�ť

    def Sale_element_phone_text(self, dr):
        return dr.find_element_by_id('customerphone')  # �����Ա�绰�ı���

    def Sale_element_msg(self, dr):
        return dr.find_element_by_xpath('//*[@id="vipsell"]/div[1]/form/div[2]/button')  # ��ѯ��Ա��Ϣ

    def Sale_element_Receivables(self, dr):
        return dr.find_element_by_id('submit')  # ȷ���տ�

    def Cancellation_element_(self,dr):
        return dr.find_element_by_xpath('//*[@id="navbar"]/ul[2]/li[2]/a')