import requests
from lxml import etree
import json
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
name_url = 'https://m.kuaidi100.com/apicenter/kdquerytools.do?method=autoComNum&text='
NO = input('请输入要查询的快递单号：')
url = name_url+NO
html_dic = json.loads(requests.get(url, headers=headers).text)
auto_dic = html_dic.get('auto')[0]

print(auto_dic.get("name"))