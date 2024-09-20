from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_drvier():
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.python.org")
    print(driver.title)
    input()
    driver.quit()

get_drvier()
