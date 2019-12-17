import scrapy
from douban_spider.items import DoubanSpiderItem
import time

class spider(scrapy.Spider):
    name = "douban_spider"
    start_urls = ["https://www.douban.com/group/586674/discussion?start=0"]
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }

    def parse(self, response):
        try:
            time.sleep(3)
            tables = response.xpath(
                "//*[@id='content']/div/div[1]/div[2]/table/tr")  # [0].strip()#/tr[2]/td[1]/a/text()
            for table in tables[1:]:
                title = table.xpath("td[1]/a/text()").extract()[0].strip()
                author = table.xpath("td[2]/a/text()").extract()[0].strip()
                item = DoubanSpiderItem(title=title, author=author)
                yield item
            # print("**********************{}".str(response).split(" "))
            next_pages = [response.xpath("//*[@id='content']/div/div[1]/div[3]/span[4]/a/@href").extract(),
                          response.xpath("//*[@id='content']/div/div[1]/div[3]/span[5]/a/@href").extract()]
            print(next_pages)
            for next_page in next_pages:
                if next_page:
                    yield scrapy.Request(url=next_page[0], callback=self.parse,headers=self.headers)

        except Exception as e:
            print(e.__traceback__)
