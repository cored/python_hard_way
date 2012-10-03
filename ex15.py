# Import the module argv from the package/library sys
from sys import argv

# Unpack the argv variable into the script and filename variable
script, filename = argv

# Open the filename passed as an argument in the command line
txt = open(filename)

# Print a message with and extrapolating the variable filename which
# contains the passed file name
print "Here's your file %r:" % filename
# Print the content of the file
print txt.read()

# Close the file after use
txt.close()

# Print another message to ask the user for the same filename
print "Type the filename again:"
# Read user's input
file_again = raw_input(">")

# Open the content of the given filename 
txt_again = open(file_again)

# Print the content of the file the user gave
print txt_again.read()

# Close the file after use
txt_again.close()
