import scrapy
import csv
import re
class DetailsSpider(scrapy.Spider):
    name = "cbsnews"
    allowed_domains = ["dutchnews.nl"]
    # f = csv.writer(open("newswebsite.csv", "wb+"))
    start_urls=[""]
    with open('//Users/xyang/Documents/cbsnews/cbsnews.csv','rb') as f:
        reader = csv.reader(f)
        for each in reader:
            urls="https://www.cbs.nl%s"%(each[2])
            start_urls.append(urls)
    def parse(self, response):
        title=response.xpath('//div[contains(@class,"col-xs-12")]/article/header/h1/text()').extract()
        # print title
        data=response.xpath('//div[contains(@class,"col-xs-12")]/article/header/section/span[contains(@class,"date")]/text()').extract()
        # print data
        link=response.xpath('//div[contains(@class,"col-xs-12")]/article/section/p/text()').extract()
        # print link
        passage=""
        for each in link:
            passage=passage+each
        print passage
        f = csv.writer(open("cbsnews_content.csv", "ab+"))
        # try:
        f.writerow([title[0],data[0],[passage]])
        print title[0],data[0],passage
        # except:
            # pass