import requests
from lxml import etree
import xlrd

start_url = 'https://www.hsbianma.com/search?keywords='
end_url = '&filterFailureCode=true'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

data = xlrd.open_workbook('hs.xlsx').sheets()[0]
col_list = data.col(0)
n = 1
for word in col_list:
    url = start_url+word.value+end_url
    html_text = requests.get(url=url,headers=headers).text
    html_tree = etree.HTML(html_text)
    results = html_tree.xpath('//tbody/tr[@class="result-grid"]')
    for result in results:
        goods_code = "".join(result.xpath('./td[1]/a/text()')).replace(" ","").replace("\n","").replace("\r","")
        goods_name = "".join(result.xpath('./td[2]/font/text()')).replace(" ","").replace("\n","").replace("\r","")
        goods_unit = "".join(result.xpath('./td[3]/text()')).replace(" ","").replace("\n","").replace("\r","")
        goods_tax = "".join(result.xpath('./td[4]/text()')).replace(" ","").replace("\n","").replace("\r","")
        supervision_conditions = "".join(result.xpath('./td[5]/text()')).replace(" ","").replace("\n","").replace("\r","")
        inspection_quarantine = "".join(result.xpath('./td[6]/text()')).replace(" ","").replace("\n","").replace("\r","")
        content = goods_code+"\t"+goods_name+"\t"+goods_unit+"\t"+goods_tax+"\t"+supervision_conditions+"\t"+inspection_quarantine+"\n"
        # print(content)
        with open('hs.txt','a',encoding='utf-8') as f:
            f.write(content)
    print('正在抓取'+str(n)+'个词')
    n += 1