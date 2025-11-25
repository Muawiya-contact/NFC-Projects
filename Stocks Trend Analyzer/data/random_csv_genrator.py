import csv
import random
from datetime import datetime, timedelta
import os

# Current folder (run from inside data/)
current_dir = os.path.abspath(os.path.dirname(__file__))

# CSV file path (directly in current folder)
file_path = os.path.join(current_dir, "sample_stock.csv")

# Create CSV with headers
with open(file_path, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])
    
    # Generate 30 days of stock data
    date = datetime(2025, 1, 1)
    price = 100  # starting price
    for _ in range(30):
        open_price = round(price + random.uniform(-2, 2), 2)
        high = round(open_price + random.uniform(0, 5), 2)
        low = round(open_price - random.uniform(0, 5), 2)
        close = round(random.uniform(low, high), 2)
        volume = random.randint(5000, 20000)
        writer.writerow([date.strftime("%Y-%m-%d"), open_price, high, low, close, volume])
        
        date += timedelta(days=1)
        price = close

print(f"Sample CSV generated at: {file_path}")
