import scrapy
from ..items import ExpresstribuneItem

class ExpressTribuneSpider(scrapy.Spider):
    page_number = 2
    name = 'express_tribune'
    start_urls = ['https://tribune.com.pk/Business?page=1']

    def parse(self,response):
        for all_news_link in response.css('ul.listing-page li div.row div.col-md-8 div.horiz-news3-caption a::attr(href)'):
            yield response.follow(all_news_link.get(), callback=self.parse_news)


    def parse_news(self, response):
        items = ExpresstribuneItem()
        
        all_news = response.css('div.storypage')

        for news in all_news:
            
                title = news.css('div.story-box-section h1::text').get()
                excerpt = news.css('div.story-box-section p.story-excerpt::text').get()
                author = news.css('div.story-box-section span.storypage-leftside div.left-authorbox span a::text').get()
                date = news.css('div.story-box-section span.storypage-leftside div.left-authorbox span::text')[1].get()
                image = news.css('div.story-box-section div.mainstorycontent-parent div.storypage-main-section2 div.storypage-rightside span.top-big-img div.story-featuredimage div.amp-top-main-img div.featured-image-global img::attr(src)').get()
                storyLocation = news.css('div.story-box-section div.mainstorycontent-parent div.storypage-main-section2 div.storypage-rightside span.story-text strong.location-names::text').get().strip()
                story = news.css('div.story-box-section div.mainstorycontent-parent div.storypage-main-section2 div.storypage-rightside span.story-text p span::text').get().strip()


                items['title'] = title
                items['excerpt'] = excerpt
                items['author'] = author
                items['date'] = date
                items['image'] = image
                items['storyLocation'] = storyLocation
                items['story'] = story

                yield items
            



    # def parse(self, response):
    #     for href in response.css('ul.listing-page > li > a::attr("href")[0]'):
    #         url = response.urljoin(href.extract())
    #         print('url', url)
    #         yield scrapy.Request(url, callback=self.parse_contents)
    
    # def parse(self, response):
    #     items = ExpresstribuneItem()

    #     all_news = response.css('ul.listing-page li')

    #     for news in all_news:
                
    #         heading = news.css('h2.title-heading::text').extract()  
    #         source = news.xpath('.//a/@href')[0].extract()
    #         text = news.xpath('.//p/text()').extract()    
    #         author = news.xpath('.//span/a/text()').extract()  
    #         time = news.xpath('.//span/text()')[1].extract()
    #         image = news.xpath('.//img/@src').extract()

    #         items['heading'] = heading
    #         items['source'] = source
    #         items['text'] = text
    #         items['author'] = author
    #         items['time'] = time
    #         items['image'] = image

    #         yield items

        # next_page = ('https://tribune.com.pk/latest?page=' + str(ExpressTribuneSpider.page_number))  

        # if ExpressTribuneSpider.page_number < 6:
        #     ExpressTribuneSpider.page_number += 1
        #     yield response.follow(next_page, callback = self.parse)
