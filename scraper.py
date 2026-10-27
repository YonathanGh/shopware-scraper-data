import os
import csv
import requests
from datetime import datetime

# Using timeapi.io as it is online and highly reliable
TIME_API_URL = "https://timeapi.io"

def crawl_and_save():
    # Default values in case the network fails completely
    formatted_date = datetime.utcnow().strftime("%d.%m.%Y")
    formatted_time = datetime.utcnow().strftime("%H:%M:%S")
    
    try:
        print("Fetching current time from cloud API...")
        response = requests.get(TIME_API_URL, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            # Parse response from timeapi.io
            # Example response formats: date="10/27/2026", time="14:19"
            raw_date = data.get("date", "") # MM/DD/YYYY
            raw_time = data.get("time", "") # HH:MM
            seconds = datetime.utcnow().strftime("%S") # Fallback seconds
            
            if raw_date and raw_time:
                # Reformat MM/DD/YYYY into DD.MM.YYYY
                month, day, year = raw_date.split("/")
                formatted_date = f"{day.zfill(2)}.{month.zfill(2)}.{year}"
                formatted_time = f"{raw_time}:{seconds}"
                print("Successfully parsed live API clock data.")
        else:
            print(f"API down (Status {response.status_code}). Using system clock fallback.")
            
    except Exception as e:
        print(f"Network warning: {e}. Using system clock fallback instead.")

    # Save the file securely to the workspace path
    csv_file = "data.csv"
    print(f"Writing timestamp values -> Date: {formatted_date}, Time: {formatted_time}")
    
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Time"])
        writer.writerow([formatted_date, formatted_time])
        
    print("data.csv file written to disk successfully!")

if __name__ == "__main__":
    crawl_and_save()
