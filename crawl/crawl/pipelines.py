from scrapy.pipelines.images import ImagesPipeline
from .items import CrawlMangaItem


class CustomWikiImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        # fold = request.url.split('/')[-2]
        chapter = CrawlMangaItem(item).get("chapter")
        return '/%s/%s' % (chapter, request.url.split('/')[-1].split("?")[0])
