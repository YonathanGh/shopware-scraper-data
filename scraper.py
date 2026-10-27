import os
import csv
import requests

# Free time API
TIME_API_URL = "http://worldtimeapi.org"

def crawl_and_save():
    try:
        print("Fetching current time from cloud API...")
        response = requests.get(TIME_API_URL).json()
        datetime_str = response["datetime"] # Example: 2026-10-27T14:19:00.12345
        
        # Split into date and time parts
        date_part, time_part = datetime_str.split("T")
        year, month, day = date_part.split("-")
        
        # Format as requested: dd.mm.yyyy and hh:mm:ss
        formatted_date = f"{day}.{month}.{year}"
        formatted_time = time_part.split(".")[0] # Extracts just hh:mm:ss
        
        print(f"Time parsed: {formatted_date} at {formatted_time}")
        
        # Save straight to the root CSV file
        csv_file = "data.csv"
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time"])
            writer.writerow([formatted_date, formatted_time])
            
        print("data.csv updated successfully!")
    except Exception as e:
        print(f"Error executing script: {e}")

if __name__ == "__main__":
    crawl_and_save()
