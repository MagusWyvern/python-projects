from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Your ChromeDriver PATH
PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Navigate to the webpage
driver.get("https://mrsmgemencheh.edu.my/ePelajar/Login.asp")

# Locate the form
main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/form/div[1]/input[1]"))
        )

# Put your matrix number here
main.send_keys("")

# Put your IC number here
driver.find_element_by_xpath("/html/body/div/form/div[1]/input[2]").send_keys("")

# Click Login
driver.find_element_by_xpath("/html/body/div/form/div[1]/button").click()
time.sleep(3)

driver.find_element_by_xpath("")

input()
