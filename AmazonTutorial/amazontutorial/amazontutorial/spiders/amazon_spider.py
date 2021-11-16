# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon"
    # allowed_domains = ['amazon.com']
    start_urls = [
        "https://www.amazon.com/charts/ref=s9_acss_bw_cg_bsmlist_1a1_w?ref=bsm_char_list&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=QM5Z4081H2BS82N8FB7G&pf_rd_t=101&pf_rd_p=955e616b-c809-40fe-b48f-acce03203f88&pf_rd_i=16857165011"
    ]

    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css(".kc-rank-card-title::text").extract()
        product_author = response.css(".kc-rank-card-author::text").extract()
        # product_price = response.css("").extract()
        product_image = response.css(".not_app img::attr(src)").extract()

        items["product_name"] = product_name
        items["product_author"] = product_author
        items["product_image"] = product_image

        yield items 
