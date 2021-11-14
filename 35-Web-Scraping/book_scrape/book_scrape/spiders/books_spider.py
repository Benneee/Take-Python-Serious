import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        "http://books.toscrape.com"
    ]
    
    # Overriding the superclass start_requests method
    # With as "start_urls" class attribute, we don't need the method below anymore
    # def start_requests(self):
    #     return [
    #         scrapy.Request(url = "http://books.toscrape.com", callback = self.parse)
    #     ]
     
    # response.body # this gives us the raw HTML content of the website we want to scrape        
    def parse(self, response):
        # titles = response.css("article.product_pod h3 a::attr(title)").getall()
        # prices = response.css("article.product_pod p.price_color::text").getall()
        # for title in titles:
        #     yield { "title": title }
        
        # Easier syntax
        for entry in response.css("article.product_pod"):
            title = entry.css("h3 a::attr(title)").get()
            price = entry.css("p.price_color::text").get()
            
            yield { "title": title, "price": price }
            
            next_page = response.css("li.next a::attr(href)").get()
            
            if next_page is not None:
                next_page_url = response.urljoin(next_page)
                yield scrapy.Request(url = next_page_url, callback = self.parse)
        