import scrapy
from scrapy.crawler import CrawlerProcess


class TestSpider(scrapy.Spider):
    name = 'test'
    # start_urls = ['https://books.toscrape.com',
    #               'https://quotes.toscrape.com']


    custom_settings = { 'DOWNLOAD_DELAY': 1 }
        


    def start_requests(self):
        urls = ['https://books.toscrape.com']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
          
        books = response.xpath("//article[@class='product_pod']")
        for book in books:
            link = 'https://books.toscrape.com/'+book.xpath(".//h3/a/@href").get()
            title = book.xpath(".//h3/a/@title").get()
            results = {
                'links': link,
                'titles':title
            }
            yield results
        
        


if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'data.csv'
    })
    process.crawl(TestSpider)
    process.start()

