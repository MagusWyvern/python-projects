from selenium import webdriver
import time

browser = webdriver.Firefox()

# Open the page
browser.get('SERVER_IP_HERE')

time.sleep(5)

currentTime = str(time.strftime("%Y%m%d%H%M%S"))

fileName = ".//scale-union//" + currentTime + '.png'

browser.save_screenshot(fileName)

