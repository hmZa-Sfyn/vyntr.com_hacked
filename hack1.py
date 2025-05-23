import requests
import json
import uuid
from tabulate import tabulate
from termcolor import colored

url = "https://vyntr.com/api/search"
params = {"q": "harry potter"}
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://vyntr.com/search?q=harry%20potter",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Ch-Ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
}

try:
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    response_json = response.json()

    if "web" in response_json and isinstance(response_json["web"], list):
        table_data = []
        for item in response_json["web"]:
            favicon = item.get("favicon", "N/A")
            title = item.get("title", "N/A")
            url = item.get("url", "N/A")
            pageTitle = item.get("pageTitle", "N/A")
            date = item.get("date", "N/A")
            preview = item.get("preview", "N/A")
            score = item.get("score", "N/A")
            nsfw = item.get("nsfw", "N/A")

            table_data.append([
                colored(title, "cyan"),
                colored(url, "green"),
                colored(pageTitle, "yellow"),
            ])

        headers = [
            colored("Title", "cyan"),
            colored("URL", "green"),
            colored("Page Title", "yellow"),

        ]

        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    else:
        print("No 'web' results found or 'web' is not a list.")

    filename = str(uuid.uuid4()) + ".json"
    with open(filename, "w") as f:
        json.dump(response_json, f, indent=4)
    print(f"Response saved to {filename}")


except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except json.JSONDecodeError:
    print("Failed to decode JSON response")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
