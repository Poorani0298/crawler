from scrapy import Spider
from scrapy.http import Request

class BooksSpider(Spider):
    name ='books'
    allowed_domains = ['books.toscrape.com/']
    start_urls = ['http://books.toscrape.com']
    def parse(self, response):
    	pass
      
