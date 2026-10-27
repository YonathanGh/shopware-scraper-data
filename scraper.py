import os
import csv
import requests

TIME_API_URL = "http://worldtimeapi.org"

def crawl_and_save():
    try:
        print("Fetching current time from cloud API...")
        response = requests.get(TIME_API_URL)
        
        # Check if the API request worked
        if response.status_code != 200:
            print(f"API Error! Status code: {response.status_code}")
            return
            
        data_json = response.json()
        datetime_str = data_json["datetime"] 
        
        # Split into date and time parts
        date_part, time_part = datetime_str.split("T")
        year, month, day = date_part.split("-")
        
        formatted_date = f"{day}.{month}.{year}"
        formatted_time = time_part.split(".")[0] # Extracts just hh:mm:ss safely
        
        print(f"Time parsed: {formatted_date} at {formatted_time}")
        
        # Force the file to save directly in the current workspace directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file = os.path.join(current_dir, "data.csv")
        
        print(f"Saving file to: {csv_file}")
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time"])
            writer.writerow([formatted_date, formatted_time])
            
        print("data.csv created successfully!")
        
    except Exception as e:
        print(f"Error executing script: {e}")

if __name__ == "__main__":
    crawl_and_save()
