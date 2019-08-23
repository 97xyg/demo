#-*-coding:utf-8-*-
"""
@project：python_file
@author：Lorus or Geek
@file：main.py
@ide：PyCharm
@time：2019-08-01 15:40:09
"""
import unittest,ddt,requests,time
from HTMLTestRunner2 import HTMLTestRunner
from study_hard.interface_test.iwebshop.getdate.get_data import data


@ddt.ddt
class Iwebshop(unittest.TestCase):


    def login(self):
        #定义一个登陆方法，用于拿到cookie
        s = requests.session()
        url = 'http://192.168.6.88:8083/iwebshop4.6/index.php?controller=simple&action=login_act'
        datas = {'login_info':'lency1','password':'123456'}
        s.post(url,datas)
        return s


    @ddt.data(*data(r'D:\python_file\study_hard\interface_test\iwebshop\data\iwebshop.xlsx'))
    @ddt.unpack
    def test_case(self,li,dic):
        module = li[0]       #模块名字
        method = li[-3].lower()    #请求方式
        expected = li[-1]   #预期结果
        new_data = dic      #post请求要传入的数据
        new_url = li[3]     #url地址
        print(new_url)
        if module not in '登录'and method in 'get':
            s = self.login()
            actual = s.get(new_url).text  #实际结果
            self.assertIn(expected,actual)
        elif module not in '登录'and method in 'post':
            s = self.login()
            actual = s.post(new_url,new_data).text  # 实际结果
            self.assertIn(expected, actual)
        else:
            actual = requests.post(new_url, new_data).text  # 实际结果
            self.assertIn(expected, actual)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Iwebshop))
    times = time.strftime('%Y_%m_%d')
    with open(f'../report/{times}_report.html', 'wb') as f:
    # with open(f'report/{times}_report.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f, title=u'Iwebshop',
                                description=u"登录加添加购物车")
        runner.run(suite)