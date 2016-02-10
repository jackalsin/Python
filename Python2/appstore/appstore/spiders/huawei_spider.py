import scrapy
import re # Regular expression operations
from scrapy.selector import Selector
from appstore.items import AppstoreItem
#from AppleStore.item import AppstoreItem# # this line from the video tutorial


class HuaweiSpider(scrapy.Spider):
    name = "huawei"
    allowed_domains = ["huawei.com"]
    
    start_url = [
        "http://appstore.huawei.com/more/all"
    ]
    
    def parse():                    
        page = Selector(response)
        
        divs = page.xpath('//div[@class = "game-info whole"]')
        
        for div in divs:
            item = AppstoreItem()
            item["item"] = div.xpath('.//h4[@class="title"]/a/text()').  \
                extract_first().encode('utf-8')
            item['url'] = div.xpath('.//h4[@class="title"]/a/@href').extract_first()
            appid = re.match(r'http://.*/(.*)', item['url']).group(1)
            # maybe something wrong upline
            item['appid'] = appid
            item['intro'] = div.xpath('.//p[@class="content"]/text()'). \
                extract_first().encode('utf-8')
            yield item
                   


            



        
