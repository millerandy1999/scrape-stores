# Request the search term from the user
print("Search: ", end='')
searchTerm = input()

# Output file
outputFile = "output1.html"
# Clear the previous output entries
open(outputFile, 'w').close()

# Make the html head that opens the CSS
head = """<!DOCTYPE html>
<html>
    <head>
        <link href=\"./css/main-light.css\" rel=\"stylesheet\" type=\"text/css\"/>
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
    </head>"""
with open(outputFile, "a") as file:
    # Add the head and start the body
    file.write(head + "\n<body>\n")