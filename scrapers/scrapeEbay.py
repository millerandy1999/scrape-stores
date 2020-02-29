# Scrapes search result data from Mercari

from bs4 import BeautifulSoup
import requests
import re
import json
import csv

from initialize import searchTerm
from initialize import outputFileCSV

urlMain = 'https://www.ebay.com'
url = 'https://www.ebay.com/sch/' + searchTerm
print("Search results from: " + url)

# Prevent 403 error
headers = {'User-Agent':'Mozilla/5.0'}

# Request the webpage
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

# Limit the soup to just the items section of the webpage
page = soup.find('ul', class_='srp-results')

# Get each item listing on the page
for item in page.find_all('li', class_='s-item'):
    #print(item.prettify())
    
    imageURL = item.find('a').find('img')['src']
    
    name = '';
    
    desc = item.find('h3').text;
    
    itemURL = item.find('a', class_="s-item__link")['href'];
    
    price = item.find('span', class_="s-item__price").text[1:];
    if " " in price:
        price = item.find('span', class_="s-item__price").text[1:].split(' ')[0];
    
    vendor = "Ebay"
    
    # Add the elements to the output file
    with open(outputFileCSV, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name, desc, imageURL, itemURL, price, vendor])