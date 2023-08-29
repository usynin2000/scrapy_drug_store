import time
import uuid

import scrapy

from aptekascraper.items import ProductItem


class AdultToothpasteSpider(scrapy.Spider):
    name = "adulttoothpastespider"
    allowed_domains = ["apteka-ot-sklada.ru"]
    start_urls = ["https://apteka-ot-sklada.ru/tomsk/catalog/sredstva-gigieny/"
                  "uhod-za-polostyu-rta/pasty-zubnye-vzroslym"]
    custom_settings = {
        'FEEDS': {
            'adult_toothpaste.json': {'format': 'json', 'overwrite': True},
        }
    }

    def parse(self, response):
        cards = response.css('div.goods-grid__inner div.ui-card')
        for card in cards:
            url = f'https://{self.allowed_domains[0]}' + card.css(
                'div.goods-card__name a ::attr(href)'
                ).get()
            yield response.follow(url, callback=self.parse_product)

        next_page = response.css(
            'li.ui-pagination__item_next a ::attr(href)'
            ).get()
        if next_page is not None:
            next_page_url = f'https://{self.allowed_domains[0]}' + next_page
            yield response.follow(next_page_url, callback=self.parse)

    def parse_product(self, response):
        product_item = ProductItem()

        product_item['timestamp'] = int(time.time())

        product_item['RPC'] = str(uuid.uuid4())

        product_item['url'] = response.url

        product_item['title'] = response.css('h1 span ::text').get()

        product_item['marketing_tags'] = []

        product_item['brand'] = response.xpath(
            "//span[@itemtype='location']/following-sibling::span/text()"
            ).get()

        product_item['section'] = response.css(
            'ul.ui-breadcrumbs__list ::text'
            ).getall()

        product_item['price_data'] = response.css(
            'div.pickpoint-row__cost ::text'
            ).get()

        product_item['stock'] = response.css(
            'div.goods-offer-panel ul li a span.ui-link__text ::text'
            ).get()

        product_item['assets'] = (
            f'https://{self.allowed_domains[0]}'
            + response.css(
                'div.goods-gallery__active-picture-area img'
                ).attrib['src']
            )

        product_item['metadata'] = response.css(
            'div.custom-html ::text'
            ).getall()

        product_item['variants'] = 1

        yield product_item
