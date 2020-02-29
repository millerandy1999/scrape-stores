# Scrapes search result data from Mercari

from bs4 import BeautifulSoup
import requests
import re
import json
import csv

from initialize import searchTerm
from initialize import outputFileCSV

urlMain = 'https://www.amazon.com'
url = 'https://www.amazon.com/s?k=' + searchTerm
print("Search results from: " + url)

# Prevent 403 error
headers = {'User-Agent':'Mozilla/5.0'}

# Request the webpage
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

print(soup.prettify())

# Limit the soup to just the items section of the webpage
page = soup.find('div', class_='s-result-list s-search-results')

#print(page.prettify())

# Get each item listing on the page
for item in page.find_all('div', class_='sg-col-4-of-24'):
    print(item.prettify())