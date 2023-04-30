#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2023

@author: yassine
"""

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def scrape_url(url, driver):
    driver.get(url)

    wait = WebDriverWait(driver, 120)  # Increase wait time to 120 seconds

    try:
        # Scrape product titles, prices, and images
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//h2[@class="jsx-2215887932 title"]')))
        prices = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//section[@class="jsx-2808635036 prices"]/span')))
        images = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="jsx-2215887932 image"]/img')))

        # Print scraped data
        for i in range(len(elements)):
            print(f"Title: {elements[i].text}")
            print(f"Price: {prices[i].text}")
            print(f"Image URL: {images[i].get_attribute('src')}")
            print()
    except TimeoutException:
        print(f"TimeoutException occurred for URL: {url}")
        print("Retrying...")
        scrape_url(url, driver)

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = uc.Chrome(executable_path='/home/yassine/Downloads/chromedriver', options=options)

urls = [
    "https://www.marjane.ma/product/465-fruits-secs",
    "https://www.marjane.ma/product/272-l%C3%A9gumes",
    "https://www.marjane.ma/product/1430-l%C3%A9gumes-pr%C3%A9par%C3%A9s",
    "https://www.marjane.ma/product/273-salades-herbes-fra%C3%AEches",
    "https://www.marjane.ma/product/307-condiments-en-vrac-conditionn%C3%A9",
    "https://www.marjane.ma/product/775-voir-tous-les-produits-fruits-l%C3%A9gumes",
    "https://www.marjane.ma/product/274-boucherie",
    "https://www.marjane.ma/product/275-volailles",
    "https://www.marjane.ma/product/774-voir-tous-les-produits-boucherie-volaille",
    "https://www.marjane.ma/product/468-fromage-%C3%A0-la-d%C3%A9coupe",
    "https://www.marjane.ma/product/469-charcuterie-%C3%A0-la-d%C3%A9coupe",
    "https://www.marjane.ma/product/776-voir-tous-les-produits-stand-fromage-charcuterie"
]

for url in urls:
    print(f"Scraping: {url}")
    scrape_url(url, driver)
    print()

driver.quit()
