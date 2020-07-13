from tools import *
from get_data import *

if __name__ == '__main__':
    print("本工具由QJ开发，zygds(GitHub id)维护")
    print("开发日期：2020：07：12")
    print("更新日期：")
    url = input('请输入需要测试的网址：')
    print("***********正在查询当前数据库***********")
    get_database(url)
    print("***********正在查询所有tables***********")
    get_tablelist(url)
    print("***********正在查询列表***********")
    get_colums_list(url)
    dump_data(url)
