# Output file
outputFile = "output1.html"

# Close the body
with open(outputFile, "a") as file:
    file.write("</body>")
    
# Close html
with open(outputFile, "a") as file:
    file.write("\n</html>")