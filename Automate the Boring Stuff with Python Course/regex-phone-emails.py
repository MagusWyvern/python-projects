#! python3 

import re
import os
import pyperclip

# Create a regex for phone numbers

phoneRegex = re.compile(r'''(

# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

((\d\d\d) | (\(\d\d\d\)))? # area code (optional)
(\s|-) # first separator
\d\d\d # first 3 digits
- # separator
\d\d\d\d # last 4 digits
(\s|-) # separator
((ext(\.)?\s) | x) # extension word part (optional)
\d{2,5} # extension number part (optional)
)''', re.VERBOSE)

# Create a regex for email adresses

emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-z0-9_.+]+ # name part 
@ # @ symbol
[a-zA-z0-9_.+]+ # domain name
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
phoneRegexResults = phoneRegex.findall(text)
emailRegexResults = emailRegex.findall(text)

print(phoneRegexResults)
print(emailRegexResults)

