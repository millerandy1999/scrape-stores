# Scrapes search result data from Mercari

from bs4 import BeautifulSoup
import requests
import re
import json
import csv

from initialize import searchTerm
from initialize import outputFileCSV

urlMain = 'https://www.mercari.com'
url = 'https://www.mercari.com/search/?keyword=' + searchTerm
print("Search results from: " + url)

# Prevent 403 error
headers = {'User-Agent':'Mozilla/5.0'}

# Request the webpage
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

# Limit the soup to just the items section of the webpage
page = soup.find(attrs={'id': re.compile('__next')}).find('div', class_='Flex-ych44r-0 Space-cutht5-0 Container-sc-9aa7mx-0 Grid2__CellWrapper-mpt2p4-1 fAwKGe')

# Get each item listing on the page
for item in page.find_all('div', class_='Flex__Box-ych44r-1 Grid2__Col-mpt2p4-0 jyGLaB'):
    #print(item.prettify())
    
    # Use JSON to parse the script to get an array of the contents
    script = item.find('script')
    scriptText = json.loads(script.text)
    
    # get the elements from the script
    imageURL = str(scriptText['image'])
    itemURL = urlMain + str(scriptText['offers']['url'])
    price = scriptText['offers']['price']
    
    # Get the item name
    try:
        name = item.find('div', class_='withMetaInfo__EllipsisText-sc-1j2k5ln-12 withMetaInfo__BrandText-sc-1j2k5ln-14 liVzKy').text
    except:
        name = ""
        
    # Get the item description
    desc = item.find('div', class_='withMetaInfo__EllipsisText-sc-1j2k5ln-12 withMetaInfo__ProductNameText-sc-1j2k5ln-13 itCrEk').text
    
    vendor = "Mercari"
    
    # Add the elements to the output file
    with open(outputFileCSV, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name, desc, imageURL, itemURL, price, vendor])