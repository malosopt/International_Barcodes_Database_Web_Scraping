import scrapy
import re

for i in range(100000,200):
    print(i)



class BarcodesSpiderSpider(scrapy.Spider):
    name = 'barcodes_spider'
    allowed_domains = ['https://barcodesdatabase.org/']
    
    urls = []
    for i in range(0,100000,200): 
        urls.append(f'https://barcodesdatabase.org/selected-products/?pa={i}&sort_options=&country_list_select=')

    start_urls = urls#['https://barcodesdatabase.org/selected-products/']



    # Configuraciones
    custom_settings = {

        'FEED_URI' : 'barcodes10.json', 
        'FEED_FORMAT' : 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'CONCURRENT_REQUESTS' : 10 #ScraperAPI  
        #'RETRY_TIMES': RETRY_TIMES, # ScraperAPI Recommendation
        #'ROBOTSTXT_OBEY' : False,
        #'CONCURRENT_REQUESTS_PER_IP' : C_R_PER_IP_PUBLISHER #ScraperAPI  
        
    }

    def parse(self, response):

        barcodes = response.css("tbody#list-products-body tr td a::attr(href)").re('[0-9]{13}')
        print(barcodes)
        yield {
            'bcode':barcodes
        }

