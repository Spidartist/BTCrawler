import scrapy


class CrawlMangaItem(scrapy.Item):
    image_urls = scrapy.Field()
    chapter = scrapy.Field()
