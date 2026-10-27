import os
import csv
import requests
from bs4 import BeautifulSoup

# 1. Target URL to crawl (using a dummy site as an example)
URL = "https://toscrape.com"

def crawl_and_save():
    print("Crawling website...")
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 2. Extract your data (Customize this part for your specific website targets)
    quotes = soup.find_all("div", class_="quote")
    
    scraped_data = []
    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        scraped_data.append([text, author])
        
    # 3. Save or Update the CSV file
    csv_file = "data.csv"
    file_exists = os.path.isfile(csv_file)
    
    # Open file ('w' to refresh entirely, or 'a' if you want to append new rows daily)
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write headers
        writer.writerow(["Content", "Author"])
        # Write rows
        writer.writerows(scraped_data)
        
    print("CSV updated successfully!")

if __name__ == "__main__":
    crawl_and_save()
