from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract

#Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

driver = webdriver.Chrome()


try:
    driver.get("https://www.google.com")
    driver.maximize_window()
    
finally:
    driver.quit()