#-*-coding:utf-8-*-
"""
@project：python_file
@author：Lorus or Geek
@file：get_data.py
@ide：PyCharm
@time：2019-08-01 16:01:38
"""
import xlrd

def data(file):
    with xlrd.open_workbook(file,encoding_override='utf-8')as book:
        sheet = book.sheets()[0]
        new_li = []
        for i in range(1,sheet.nrows):
            li = sheet.row_values(i)
            # print(li)
            dic = {}
            #get请求没有要提交的参数，避免切割时出现列表越界
            try:
                data = li[-2].split('\n')
                # print(data)
                for j in data:
                    str = j.split('=')
                    # print(str)
                    dic[str[0]] = str[1]
                # print(dic)
                old_li = [li,dic]
                new_li.append(old_li)

            except:
                # pass
                old_li = [li, dic]
                new_li.append(old_li)
        # print(new_li)
        return new_li








if __name__ == '__main__':
    data(r'D:\python_file\study_hard\interface_test\iwebshop\data\iwebshop.xlsx')