import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd 


class YahooScrapingItem(scrapy.Item):
    stock_name = scrapy.Field()
    # stock_symbol = scrapy.Field()
    intraday_price = scrapy.Field()
    change = scrapy.Field()
    # percent_change = scrapy.Field()
    volume = scrapy.Field()
    market_cap = scrapy.Field()
    pass


class TestSpider(scrapy.Spider):
    name = 'mostactive'
    
    custom_settings = { 'DOWNLOAD_DELAY': 1 }
    
    def start_requests(self):
        urls = ['https://finance.yahoo.com/most-active?.tsrc=fin-srch']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_stocks)
    
    def get_stocks(self, response):
        stocks = response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[1]/a/text()').extract()
        print(len(stocks))
        for stock in stocks:
            url = f"https://finance.yahoo.com/quote/{stock}?p={stock}"
            print("Loading "+url)
            yield scrapy.Request(url = url, callback=self.parse)  
           
    def parse(self,response):
        items = YahooScrapingItem()

        items['stock_name'] = response.xpath("//div[@id='quote-header-info']/div[2]//h1/text()").extract()
        items['intraday_price'] = response.xpath("//*[@id='quote-header-info']/div[3]/div[1]/div/span[1]/text()").extract()
        items['change'] = response.xpath("//*[@id='quote-header-info']/div[3]/div[1]/div/span[2]/text()").extract()
        items['volume'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/span/text()').extract()
        items['market_cap'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]/span/text()').extract()
    
        yield items
    

if __name__ == "__main__":
    file = 'most-active.csv'
    format = 'csv'
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEEDS':  {
            file: {'format': format},
        }
    })
    process.crawl(TestSpider)
    process.start()

