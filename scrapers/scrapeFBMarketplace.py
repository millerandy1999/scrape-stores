# Scrapes search result data from FB Marketplace

from bs4 import BeautifulSoup
import requests
import re
import json
import csv

from initialize import searchTerm
from initialize import outputFileCSV

urlMain = 'https://www.facebook.com'
url = 'https://www.facebook.com/marketplace/search/?query=' + searchTerm
print("Search results from: " + url)

# Prevent 403 error
headers = {'User-Agent':'Mozilla/5.0'}

# Request the webpage
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

# Limit the soup to just the items section of the webpage
page = soup.find('div', class_='bq4bzpyk j83agx80 btwxx1t3 lhclo0ds jifvfom9 muag1w35 dlv3wnog enqfppq2 rl04r1d5')

print(soup.prettify())