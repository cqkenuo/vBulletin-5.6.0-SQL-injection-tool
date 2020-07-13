from tools import *
from get_data import *

if __name__ == '__main__':
    url = input('请输入需要测试的网址：')
    print("***********正在查询当前数据库***********")
    get_database(url)
    print("***********正在查询所有tables***********")
    get_tablelist(url)
    print("***********正在查询列表***********")
    get_colums_list(url)
    dump_data(url)
