# 12/06/2021
# Miguel Angel Sanchez
# From COlOMBIA
# @15novmasr Instagram
# @15Once94 Twitter

import scrapy
import re


class BarcodesSpiderSpider(scrapy.Spider):

    name = 'barcodes_spider'
    allowed_domains = ['https://barcodesdatabase.org/']
    
    urls = []

    for i in range(0,100000,200): 
        urls.append(f'https://barcodesdatabase.org/selected-products/?pa={i}&sort_options=&country_list_select=')

    start_urls = urls #['https://barcodesdatabase.org/selected-products/']


    #Settings
    custom_settings = {

        'FEED_URI' : 'barcodes.json', # if you want a csv file, put barcodes.json
        'FEED_FORMAT' : 'json',       # if you want a csv file, just change 'json' by 'csv'
        'FEED_EXPORT_ENCODING': 'utf-8',
        'CONCURRENT_REQUESTS' : 2 , 
        'RETRY_TIMES': 4 ,
        'ROBOTSTXT_OBEY' : True 
        
    }


    def parse(self, response):

        barcodes = response.css("tbody#list-products-body tr td a::attr(href)").re('[0-9]{13}')
        #print(barcodes)
        yield {
                'bcode':barcodes
              }
