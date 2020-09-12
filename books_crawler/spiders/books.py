from scrapy import Spider
from scrapy.http import Request

class BooksSpider(Spider):
	name ='books'
	allowed_domains = ['books.toscrape.com/']
	start_urls = ['http://books.toscrape.com']

	def parse(self, response):
		books = response.xpath('//h3/a/@href').extract()
		print('start')
		print(books)
		print('end')
		responses = []
		for book in books:
			absolute_url= response.urljoin(book)
			print('start')
			print(absolute_url)
			print('end')
			responses.append(Request(absolute_url, callback=self.parse_book))

		print(responses)

	def parse_book(self, response):
		pass
