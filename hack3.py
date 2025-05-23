import requests
import json

url = "https://vyntr.com/api/search?q=harry%20potter"
payload = {"q": "harry potter"}

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

    print("Request URL:", response.url)
    print("Request Method:", response.request.method)
    print("Status Code:", response.status_code)
    print("Remote Address:", response.raw._connection.sock.getpeername())
    print("Referrer Policy:", response.headers.get("Referrer-Policy", "N/A"))

    print("\\nResponse Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    print("\\nRequest Headers:")
    for key, value in response.request.headers.items():
        print(f"{key}: {value}")

    print("\\nPayload:")
    print(json.dumps(payload, indent=4))

    print("\\nResponse Content:")
    try:
        print(json.dumps(response.json(), indent=4))
    except json.JSONDecodeError:
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
