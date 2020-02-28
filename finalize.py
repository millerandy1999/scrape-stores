# Adds more html elements at the bottom of the page

from initialize import outputFile

footer = """<footer>Created by Andy Miller. For personal use only.</footer>"""
# Add the footer
with open(outputFile, "a") as file:
    file.write(footer + "\n")

# Close the body
with open(outputFile, "a") as file:
    file.write("</body>")
    
# Close html
with open(outputFile, "a") as file:
    file.write("\n</html>")