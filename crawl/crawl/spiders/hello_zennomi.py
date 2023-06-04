from crawl.items import CrawlMangaItem
import scrapy
START_IDX = 0
END_IDX = 60

class GrandBlueSpider(scrapy.Spider):
    name = 'hello'
    start_urls = ['https://blogtruyen.vn/19821/hello-hello-and-hello']

    # def parse(self, response):
    #     chapter_urls = response.css('#list-chapters>p>span.title>a::attr(href)').getall()
    #     for url in chapter_urls:
    #         chapter = response.urljoin(url)
    #
    #     raw_image_urls = response.css("#content > img::attr(src)").getall()
    #     yield CrawlMangaItem(image_urls=raw_image_urls, chapter=response.request.url[-9:])
    #
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)

    def parse(self, response):
        # list-chapters
        for url in response.css('#list-chapters>p>span.title>a::attr(href)').getall()[START_IDX:]:
        # for url in ['https://blogtruyen.vn/c783215/grand-blue-chapter-835']:
            chapter = response.urljoin(url)
            yield scrapy.Request(chapter, callback=self.parse_item)

    def parse_item(self, response):
        raw_image_urls = response.css("#content > img::attr(src)").getall()
        yield CrawlMangaItem(image_urls=raw_image_urls, chapter=response.request.url.split("/")[-1])
