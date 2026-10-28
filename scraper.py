import os
import csv
import requests
from datetime import datetime
# We use a built-in library to shift time zones
import zoneinfo 

TIME_API_URL = "https://timeapi.io"

def crawl_and_save():
    # Force the backup clock to use Germany's local time zone
    berlin_tz = zoneinfo.ZoneInfo("Europe/Berlin")
    now_in_germany = datetime.now(berlin_tz)
    
    formatted_date = now_in_germany.strftime("%d.%m.%Y")
    formatted_time = now_in_germany.strftime("%H:%M:%S")
    
    try:
        print("Fetching current time from cloud API...")
        response = requests.get(TIME_API_URL, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            raw_date = data.get("date", "") # MM/DD/YYYY
            raw_time = data.get("time", "") # HH:MM
            seconds = now_in_germany.strftime("%S") 
            
            if raw_date and raw_time:
                month, day, year = raw_date.split("/")
                formatted_date = f"{day.zfill(2)}.{month.zfill(2)}.{year}"
                formatted_time = f"{raw_time}:{seconds}"
                print("Successfully parsed live German clock data.")

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
