import requests
from lxml import etree
# 初始化数据
base_url = 'http://kaijiang.500.com/shtml/dlt/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
# 获取开奖期url数据
req = requests.get(url=base_url,headers=headers)
req.encoding = req.apparent_encoding
req_text = req.text
html_tree = etree.HTML(req_text)
urls = html_tree.xpath('//div[@class="iSelectList"]/a/@href')
# 获取开奖号码，及一等奖的中奖人数
for url in urls:
    date = url.split('/')[-1].split('.')[0]
    data_req = requests.get(url=url,headers=headers)
    data_req.encoding = data_req.apparent_encoding
    data_req_text = data_req.text
    data_tree = etree.HTML(data_req_text)
    ball_list = data_tree.xpath('//div[@class="ball_box01"]')
    for ball in ball_list:
        red01 = "".join(ball.xpath('./ul/li[@class="ball_red"][1]/text()'))
        red02 = "".join(ball.xpath('./ul/li[@class="ball_red"][2]/text()'))
        red03 = "".join(ball.xpath('./ul/li[@class="ball_red"][3]/text()'))
        red04 = "".join(ball.xpath('./ul/li[@class="ball_red"][4]/text()'))
        red05 = "".join(ball.xpath('./ul/li[@class="ball_red"][5]/text()'))
        blue01 = "".join(ball.xpath('./ul/li[@class="ball_blue"][1]/text()'))
        blue02 = "".join(ball.xpath('./ul/li[@class="ball_blue"][2]/text()'))
        content = date+'\t'+red01+'\t'+red02+'\t'+red03+'\t'+red04+'\t'+red05+'\t'+blue01+'\t'+blue02+'\n'
        print(content)
        # 写入文件
        with open('ball.txt','w') as f:
            f.write(content)