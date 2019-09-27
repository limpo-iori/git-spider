import requests
from lxml import etree
import json
import xlrd
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
name_url = 'https://m.kuaidi100.com/apicenter/kdquerytools.do?method=autoComNum&text='
xlsx_date = xlrd.open_workbook('no.xlsx').sheets()[0]
NOS = xlsx_date.col(0)
for NO in NOS:
	url = name_url+NO.value
	html_dic = json.loads(requests.get(url, headers=headers).text)
	err_NO = []
	expSpellName_dic ={'圆通速递':'yuantong','韵达快递':'yunda'}
	try:
		auto_dic = html_dic.get('auto')[0]
		name = auto_dic.get("name")
		exp_url = 'https://biz.trace.ickd.cn/'+expSpellName_dic.get(name)+'/'+NO.value+'?'
		message = json.loads(requests.get(exp_url, headers=headers).text)
		datas = message.get('data')
		for data in datas:
			print(NO.value+'\t'+data.get('time')+'\t'+data.get('context'))
		print('\n\n')
	except:
		print('快递单号错误')
		err_NO.append(NO)
print(err_NO)
