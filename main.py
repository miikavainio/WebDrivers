from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

#Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# driver = webdriver.Chrome()


try:
    driver.get("https://www.google.com")
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "W0wltc"))
    ).click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    screenshot = "screenshot.png"
    driver.save_screenshot(screenshot)
    print(f"Screenshot saved")
    
    imagee = Image.open(screenshot)
    text = pytesseract.image_to_string(imagee)
    
    text_path = "text.txt"
    with open(text_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)
    print(f"Text saved")
    
finally:
    driver.quit()