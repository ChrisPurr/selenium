import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get("https://www.seleniumeasy.com/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "edit-search-block-form--2"))
    )
    element.send_keys("test" + Keys.ENTER)
    
except:
    driver.quit()