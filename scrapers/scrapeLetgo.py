# Scrapes search result data from Letgo

from bs4 import BeautifulSoup
import requests
import re
import json
import csv

from initialize import searchTerm
from initialize import outputFileCSV

urlMain = 'https://www.letgo.com'
url = 'https://www.letgo.com/en-us?searchTerm=' + searchTerm
print("Search results from: " + url)

# Prevent 403 error
headers = {'User-Agent':'Mozilla/5.0'}

# Request the webpage
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

