import requests
from lxml import etree

class RenrenSpider():
    def __init__(self):
        self.url='http://www.renren.com/971924428/profile'
        self.headers={
            # 'Cookie':'anonymid=jzc4akkfjayzkd; depovince=GW; _r01_=1; JSESSIONID=abcCJ1ceSU711_qQ6stYw; ick_login=feb70a3a-fb5b-4eec-8af4-74cccd863cf7; t=2e0274329a340e0e76a47668a346f34d8; societyguester=2e0274329a340e0e76a47668a346f34d8; id=971924428; xnsid=6cb204bd; jebecookies=3acf2d9f-3c8e-4a05-a5a2-7a763e1350b9|||||; ver=7.0; loginfrom=null; jebe_key=25814ad1-7760-4a51-bb6d-b30258bd4641%7C47fa46d7577188c4aa880c86d35df0bc%7C1565839458098%7C1%7C1565839458024; jebe_key=25814ad1-7760-4a51-bb6d-b30258bd4641%7C47fa46d7577188c4aa880c86d35df0bc%7C1565839458098%7C1%7C1565839458030; wp_fold=0',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
        }
    def get_html(self):
        html=requests.get(url=self.url,headers=self.headers).text
        self.parse_html(html)
    def parse_html(self,html):
        # parse_html=etree.HTML(html)
        # r_list=parse_html.xpath('')
        print(html)

if __name__ == '__main__':
    spider=RenrenSpider()
    spider.get_html()























