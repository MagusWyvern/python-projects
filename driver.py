from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://mrsmgemencheh.edu.my/ePelajar/Login.asp")

main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/form/div[1]/input[1]"))
        )
main.send_keys("NG190041")
driver.find_element_by_xpath("/html/body/div/form/div[1]/input[2]").send_keys("060610160023")
driver.find_element_by_xpath("/html/body/div/form/div[1]/button").click()
time.sleep(3)
driver.find_element_by_xpath("")

input()
