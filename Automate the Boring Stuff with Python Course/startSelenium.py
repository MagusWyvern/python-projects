# Lesson 41: Selenium WebDriver

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://automatetheboringstuff.com/')

element = driver.find_element_by_css_selector('body > div > main > div > p:nth-child(6)')

print(element.text)

print(len(element.text))

time.sleep(5)

input("Press Enter to quit...")

