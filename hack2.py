import requests
from tabulate import tabulate

# Define the URL and query parameters
url = "https://vyntr.com/api/search"
params = {"q": "what is harry potter"}

# Set up headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://vyntr.com/search?q=what%20is%20harry%20potter",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Ch-Ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
}

# Send the GET request
response = requests.get(url, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    try:
        # Parse the JSON response
        data = response.json()
        
        # Check if 'results' key exists in the response
        if 'results' in data:
            # Prepare data for tabulation
            table_data = []
            for item in data['results']:
                title = item.get('title', 'N/A')
                description = item.get('description', 'N/A')
                url = item.get('url', 'N/A')
                table_data.append([title, description, url])
            
            # Define table headers
            headers = ["Title", "Description", "URL"]
            
            # Print the table
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print("No results found in the response.")
            print(tabulate([], headers=["Title", "Description", "URL"], tablefmt="grid"))
    except ValueError:
        print("Error: Unable to parse JSON response.")
else:
    print(f"Request failed with status code: {response.status_code}")
