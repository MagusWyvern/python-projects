# Lesson 40: Parsing HTML with BeautifulSoup

import bs4
import requests

# response = requests.get('http://ngokevin.com/blog/angular-1/')

# response.raise_for_status()

# soup = bs4.BeautifulSoup(response.text, 'html.parser')

# elements = soup.select('body > div.post > p:nth-child(3)')

# print(elements[0].text.strip())

def getArticleDate(articleURL):
    response = requests.get(articleURL)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Select the date using CSS selectors
    elems = soup.select('body > div.post > p:nth-child(3)')
    return elems[0].text.strip()

date = getArticleDate('http://ngokevin.com/blog/angular-1/')

print(date)

def getAmazonPrice(productURL):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    # Make the request whilst specifying the headers so Amazon doesn't block us
    response = requests.get(productURL, headers = headers)

    response.raise_for_status()

    # Passing the text of the response to BeautifulSoup will parse it
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Select the date using CSS selectors
    elements = soup.select('#newBuyBoxPrice')

    # Return the first element
    return elements[0].text.strip()

date = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')

print(date)
