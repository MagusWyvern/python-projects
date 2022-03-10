# Lesson 39: WebDownloader

import requests

# This will return an object
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# Program will exit if the response code is not 200
response.raise_for_status()

print('The request is ' + str(response.status_code))

print('The full length of the text is ' + str(len(response.text)))

print('The preview of the text: \n' + response.text[:250])

writeToFile = open('RomeoAndJuliet.txt', 'wb')

# Write the response to the file with calls to the iter_content() method
for chunk in response.iter_content(100000):
    writeToFile.write(chunk)

writeToFile.close()

input()