import os
import csv
import requests

TIME_API_URL = "http://worldtimeapi.org"

def crawl_and_save():
    try:
        response = requests.get(TIME_API_URL).json()
        datetime_str = response["datetime"] 
        
        date_part, time_part = datetime_str.split("T")
        year, month, day = date_part.split("-")
        formatted_date = f"{day}.{month}.{year}"
        formatted_time = time_part.split(".")[0] # Get hh:mm:ss
        
        with open("data.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time"])
            writer.writerow([formatted_date, formatted_time])
        print("CSV updated with cloud time!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    crawl_and_save()
