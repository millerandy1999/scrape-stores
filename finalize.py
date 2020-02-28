# Output file
outputFile = "output1.html"

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