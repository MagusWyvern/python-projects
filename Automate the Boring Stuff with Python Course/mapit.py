# Lesson 38: MapIt

# MapIt is a simple web app that lets you create a map of where you've been.
import webbrowser, sys, pyperclip

# Check if command line arguments were passed
sys.argv 

# Verify that the command line arguments are valid
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

# If no address was passed, use the clipboard
else:
    address = pyperclip.paste()

# This will open the default browser and go to the address
webbrowser.open('https://www.google.com/maps/place/' + address)
