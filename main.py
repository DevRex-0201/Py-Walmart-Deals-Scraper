import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime

# URL of the webpage to scrape
url = 'https://www.walmart.com/shop/deals'

chrome_options = Options()
chrome_options.add_argument("--headless")
# Uncomment the following line if you want the browser to run headless
# chrome_options.add_argument("--headless")

# Replace with your own proxy details if needed
# proxy = "164.68.105.235:3128"
# chrome_options.add_argument(f'--proxy-server={proxy}')

# Replace 'chromedriver.exe' with the path to your ChromeDriver executable
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigating to the URL
driver.get(url)

# Waiting for the specific elements to be loaded on the page
try:
    element_present = EC.presence_of_element_located((By.XPATH, '//div[@data-testid="list-view"]'))
    WebDriverWait(driver, 10).until(element_present)
except Exception as e:
    print("Timed out waiting for page to load")

# Getting the page source and parsing it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find all <div> elements with data-testid="list-view"
items = soup.find_all('div', {'data-testid': 'list-view'})
print(len(items))

# Processing each item found
for item in items:
    # Extracting the image URL
    img_element = item.find('img', {'data-testid': 'productTileImage'})
    img_url = img_element['src'] if img_element else 'No image found'

    # Extracting the price
    price_div = item.find('div', {'data-automation-id': 'product-price'})
    if price_div:
        price_spans = price_div.find_all('span')
        price = price_spans[2].get_text() if len(price_spans) > 2 else "Price not found"
    else:
        price = "None"

    # Extracting the product title
    title_span = item.find('span', {'data-automation-id': 'product-title'})
    title = title_span.get_text() if title_span else 'No title found'

    # Extracting product reviews
    review_span = item.find('span', {'data-testid': 'product-reviews'})
    review = review_span.get_text() if review_span else 'No reviews'

    # Printing the extracted information
    print("Image URL: " + img_url)
    print("Price: " + price)
    print("Product Title: " + title)
    print("Product Review: " + review)
    print("\n")

# Closing the browser
driver.quit()
