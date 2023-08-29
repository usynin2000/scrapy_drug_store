# Scrapy settings for aptekascraper project
BOT_NAME = "aptekascraper"

SPIDER_MODULES = ["aptekascraper.spiders"]
NEWSPIDER_MODULE = "aptekascraper.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   "aptekascraper.pipelines.AptekascraperPipeline": 300,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
