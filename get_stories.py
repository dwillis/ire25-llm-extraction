import requests
import json
import time

def fetch_json_data(base_url, num_pages=1):
    # Define headers to mimic a Firefox browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
    }

    all_data = []  # List to hold all data collected

    # Loop over the specified number of pages
    for page in range(1, num_pages + 1):
        time.sleep(0.5)
        # Construct the URL with the current page number
        page_url = f"{base_url}?page={page}"
        
        # Fetch the JSON data from the URL
        response = requests.get(page_url, headers=headers)
        if response.status_code == 200:
            # Load JSON data from the response
            data = response.json()
            all_data.extend(data)  # Add data to the list
            print(f"Data retrieved from page {page}")
        else:
            print(f"Failed to retrieve data from page {page}: Status Code {response.status_code}")

    return all_data

# URL to the JSON data
base_url = 'https://cnsmaryland.org/wp-json/wp/v2/posts'
# Fetch JSON data from the first 10 stories
data = fetch_json_data(base_url, num_pages=1)

# Optionally, save the data to a file or handle it as needed
with open('cns_maryland_posts.json', 'w') as file:
    json.dump(data, file, indent=4)
