import requests


def my_post(www, data):
    header = {
        'Host': www,
        'User-Agent': 'curl/7.55.1',
        'Accept': '*/*',
        'Content-Length': '206',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    url = 'http://' + www + '/ajax/api/content_infraction/getIndexableContent'
    res = requests.post(url=url, data=data, headers=header, timeout=5)
    return res


def write(pwd, file):
    with open('file/' + pwd, 'a', encoding='utf8') as f:
        f.write(file)


def read(pwd):
    with open('file/' + pwd, 'r', encoding='utf8')as f:
        list = f.readlines()
        return list


def get_tbname():
    return read('table_name.txt')
