#Scraping Product information from Ecommerce Website(Flipkart) using lxml
import requests
import lxml.html

html=requests.get('https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_1')
lxml_doc=lxml.html.fromstring(html.content)

boxes=lxml_doc.xpath('//div[@class="_2pi5LC col-12-12"]')[2:]

for box in boxes:
    try:
        mob_name=box.xpath('.//div[@class="_4rR01T"]/text()')[0]
        print(f"Mobile Name: {mob_name}")
        
        rating=box.xpath('//*[@id="productRating_LSTMOBFX77NDJXMDZZY0TA0IY_MOBFX77NDJXMDZZY_"]/div/text()')[0]
        print(f"Rating : {rating}")
        
        desp=box.xpath('.//ul[@class="_1xgFaf"]')
        for each_desp in desp:
            d=each_desp.xpath('.//li[@class="rgWa7D"]/text()')
            print(f"Description: {d}")

            more=box.xpath('.//a[@class="_1fQZEK"]/@href')
            val="https://www.flipkart.com"
            print(f"More info: {val+more[0]}")
        
            print(" ")
    except:
        print(" ")