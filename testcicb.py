#!/usr/bin/python3
# -*-coding:gbk-*-
# @project：python_file
# @author：子木仄言
# @file：testci.py
# @software：PyCharm
# @time：2019/08/01 16:17:12
import os, re
import time


class Start_ci:
    # 开始获取svn服务端的代码
    def __init__(self):
        self.url = r'https://LY:888/svn/moniu/'
        self.path = r'C:\Users\笑义戈\Desktop\svn_demo'
        self.tomcat_file = r'D:\xampp\tomcat\webapps'

    def get_code(self):
        try:
            # 尝试更新路径下的文件
            # os.system(f'svn update {self.path} --username liyi --password liyi')
            os.system(f'svn update {self.path}')
        except:
            # 当没有更新成功则先checkout一下,在update
            os.system(f'svn checkout {self.url} {self.path} --username liyi --password liyi')
            os.system(f'svn update {self.path}')

    def structure(self):
        # 开始构成版本，先修改配置文件，然后编译，编译成功之后会有一个BUILD SUCCESSFUL关键字
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
                    print('编译成功')
                else:
                    print('编译失败')
            except Exception as e:
                print(f'编译异常，异常原因{e}')
        else:
            print(f'文件不齐，请检查{self.path}目录下有没有build.xml文件')

    def tomcat(self):
        # 先关闭tomcat并删除老版本的war包和目录，在将编译的安装包放置tomcat,在启动并启动tomcat
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
        self.get_code()  # 得到代码
        self.structure()  # 构建版本
        self.tomcat()

    def check_version(self):
        # 轮询机制，一旦发现新版本则开始持续集成，每5分钟检查一次
        while True:
            r = os.popen(f'svn update {self.path}').read()
            line = r.split('\n')
            if len(line) > 3:
                print('发现新版本，开始持续集成...')
                self.start()
            else:
                print('木有发现新版本啦！')
            time.sleep(3)


if __name__ == '__main__':
    start = Start_ci()
    # start.get_code() #调式代码
    # start.structure()
    # start.tomcat()
    # start.check()
    start.check_version()
