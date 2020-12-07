#Scraping Product information from Ecommerce Website(Flipkart) using BeautifulSoup and storing it in csv file
from bs4 import BeautifulSoup
import requests
import csv
import os

csv_file=open('csv_scrape.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Name','Rating','Description'])

content=requests.get('https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_1').text
soup=BeautifulSoup(content,'lxml')

box_cont=soup.find_all('div',class_="_2pi5LC col-12-12")
for cont in box_cont:
    try:
        s=''''''
        mob_name=cont.find('div',class_="_4rR01T").text
        print(f"Name : {mob_name}")
        
        try:
            rating=cont.find('div',class_="_3LWZlK").text
            print(f"Rating : {rating}")
        except:
            print("Not Rated")
            rating="Not rated"
        
        try:   
            desp=cont.find_all('li',class_="rgWa7D")
            for each_desp in desp:
                if each_desp.text:
                    print(each_desp.text) 
                    s+=each_desp.text 
                    s+=os.linesep
            csv_writer.writerow([mob_name,rating,s])
        except:
            print("No Description Available")
            s="No Description Available"
            csv_writer.writerow([mob_name,rating,s])
        print(" ")
    except:
        print(" ")
        
csv_file.close()