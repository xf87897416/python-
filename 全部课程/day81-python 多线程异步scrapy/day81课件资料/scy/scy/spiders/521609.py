# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector,XPathSelector
from scrapy.http import Request
class XiaohuarSpider(scrapy.Spider):
    name = "521609"
    allowed_domains = ["521609.com"]
    start_urls = ['http://www.521609.com/daxuexiaohua/list31.html']

    visited_set = set()

    def parse(self, response):
        self.visited_set.add(response.url)
        # 1. 当前页面的所有校花爬下来
        # 获取div并且属性为 class=item masonry_brick
        hxs = HtmlXPathSelector(response)
        item_list = hxs.select('//div[@class="index_img list_center"]')
        item_list=item_list.select('.//ul/li/a')


        for item in item_list:
            v = item.select('.//b/text()').extract_first()
            if v:
             print(v)
            v = item.select('./text()').extract_first()
            if item.select('./text()').extract_first():
                print(v)



        # print(item_list,'------------')


        # 2. 在当前页中获取 http://www.xiaohuar.com/list-1-\d+.html，
        # page_list = hxs.select('//a[@href="http://www.xiaohuar.com/list-1-1.html"]')
        # page_list = hxs.select('//a[re:test(@href,"http://www.xiaohuar.com/list-1-\d+.html")]/@href').extract()
        # for url in page_list:
        #     if url in self.visited_set:
        #         pass
        #     else:
        #         obj = Request(url=url,method='GET',callback=self.parse)
        #         yield obj
        page_list = hxs.select('//a[@href="http://www.521609.com/daxuexiaohua/list32.html"]')
        page_list = hxs.select('//a[re:test(@href,"http://www.521609.com/daxuexiaohua/list\d+.html")]/@href').extract()
        for url in page_list:
            if url in self.visited_set:
                pass
            else:
                obj = Request(url=url,method='GET',callback=self.parse)
                yield obj