import requests
import csv
import time

def scrape_gmb(category, location):
    url = f"https://nominatim.openstreetmap.org/search?q=restaurant+in+Bangalore&format=json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        with open(f'{category}_{location}_businesses.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Name', 'Address'])

            for item in data:
                name = item.get('display_name', '')
                lat = item.get('lat', '')
                lon = item.get('lon', '')
                address = item.get('address', {}).get('road', '')  # Example: 'road' key may contain street name
                phone = ''  # Unfortunately, Nominatim API does not provide phone numbers or website URLs
                website = ''

                csv_writer.writerow([name, address])

    else:
        print("Failed to retrieve data")

# Example usage:
categories = ['restaurant', 'hotel', 'gym']  # Add more categories as needed
locations = ['Bangalore']  # Add more locations as needed

for category in categories:
    for location in locations:
        scrape_gmb(category, location)
        time.sleep(1)  # To avoid hitting Nominatim's servers too frequently
