# Request the search term from the user
print("Search: ", end='')
searchTerm = input()

# Output files
outputFile = "output1.html"
outputFileCSV = "data.csv"
# Clear the previous output entries
open(outputFile, 'w').close()
open(outputFileCSV, 'w').close()

# Make the html head that opens the CSS
head = """<!DOCTYPE html>
<html>
    <head>
        <link href=\"./css/main-light.css\" rel=\"stylesheet\" type=\"text/css\"/>
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
    </head>"""
header = """        <header>
            <div class="container">
                <div id="logo">
                    <h1>StoreScrape</h1>
                </div>
            </div>
        </header>"""
with open(outputFile, "a") as file:
    # Add the head and start the body
    file.write(head + "\n<body>\n" + header + "\n")