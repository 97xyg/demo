#!/usr/bin/python3
# -*-coding:gbk-*-
# @project��python_file
# @author����ľ����
# @file��testci.py
# @software��PyCharm
# @time��2019/08/01 16:17:12
import os, re
import time


class Start_ci:
    # ��ʼ��ȡsvn����˵Ĵ���
    def __init__(self):
        self.url = r'https://LY:888/svn/moniu/'
        self.path = r'C:\Users\Ц���\Desktop\svn_demo'
        self.tomcat_file = r'D:\xampp\tomcat\webapps'

    def get_code(self):
        try:
            # ���Ը���·���µ��ļ�
            # os.system(f'svn update {self.path} --username liyi --password liyi')
            os.system(f'svn update {self.path}')
        except:
            # ��û�и��³ɹ�����checkoutһ��,��update
            os.system(f'svn checkout {self.url} {self.path} --username liyi --password liyi')
            os.system(f'svn update {self.path}')

    def structure(self):
        # ��ʼ���ɰ汾�����޸������ļ���Ȼ����룬����ɹ�֮�����һ��BUILD SUCCESSFUL�ؼ���
        conf = '''
        db_url=jdbc:mysql://localhost:3306/moniu?useUnicode=true&characterEncoding=utf8\n 
        db_username=root\n
        db_password=199703\n
        db_driver=com.mysql.jdbc.Driver'''
        with open(rf'{self.path}\WebRoot\WEB-INF\classes\db.properties', 'w', encoding='utf-8')as f:
            f.write(conf)
        file = os.listdir(self.path)
        if 'build.xml' in file:
            r = os.popen(f'ant -f {self.path}\\build.xml').read()
            try:
                par = re.compile('BUILD \w+')
                get_str = re.search(par, r).group()
                if get_str == 'BUILD SUCCESSFUL':
                    print('����ɹ�')
                else:
                    print('����ʧ��')
            except Exception as e:
                print(f'�����쳣���쳣ԭ��{e}')
        else:
            print(f'�ļ����룬����{self.path}Ŀ¼����û��build.xml�ļ�')

    def tomcat(self):
        # �ȹر�tomcat��ɾ���ϰ汾��war����Ŀ¼���ڽ�����İ�װ������tomcat,������������tomcat
        os.system(r'taskkill -f -im java.exe')
        try:
            os.system(rf'del /S /Q {self.tomcat_file}\woniusales.war')
            os.system(rf'rmdir /S /Q {self.tomcat_file}\woniusales')
        except:
            pass
        os.system(rf'copy {self.path}\moniu.war {self.tomcat_file}')
        os.system(r'd: && cd D:\xampp\tomcat\bin && startup.bat')
        time.sleep(120)

    def start(self):
        self.get_code()  # �õ�����
        self.structure()  # �����汾
        self.tomcat()

    def check_version(self):
        # ��ѯ���ƣ�һ�������°汾��ʼ�������ɣ�ÿ5���Ӽ��һ��
        while True:
            r = os.popen(f'svn update {self.path}').read()
            line = r.split('\n')
            if len(line) > 3:
                print('�����°汾����ʼ��������...')
                self.start()
            else:
                print('ľ�з����°汾����')
            time.sleep(3)


if __name__ == '__main__':
    start = Start_ci()
    # start.get_code() #��ʽ����
    # start.structure()
    # start.tomcat()
    # start.check()
    start.check_version()
