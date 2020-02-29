# Converts a CSV file to an HTML format
# name, desc, imageURL, itemURL, price, vendor

import csv
import operator

from initialize import outputFile
from initialize import outputFileCSV

f = open(outputFile, 'a')

with open(outputFileCSV, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    sortedlist = sorted(reader, key=lambda row: float(row[4]), reverse=True)
    
    for row in sortedlist:
        f.write("    <span>\n        ")
        # Image
        f.write("<img src=\"" + row[2] + "\"/>\n        ")
        # Title
        f.write("<div>" + row[0] + "</div>")
        # Description
        f.write("<a href=\"" + row[3] + "\">" + row[1] + "</a>")
        # Price
        f.write("<div>$" + row[4] + "</div>")
        
        f.write("<div id='vendor'>Source: " + row[5] + "</div>")
        f.write("\n    </span>\n")
f.close()