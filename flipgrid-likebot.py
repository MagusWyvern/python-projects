from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome WebDriver PATH location
PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Get the flipgrid video page
driver.get("https://flipgrid.com/xxxxxxxx")

# Main loop function
n = 0
while n != 1000:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div[1]/div[2]/div[1]/div/button"))
        )
    main.click()
    driver.refresh()
    time.sleep(5)
    n += 1
else:
    driver.quit()
                                                
