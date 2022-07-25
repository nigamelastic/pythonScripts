import requests

BASE_URL = "https://example.com/api/content/v1/products/search"

headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

params = {
    "page": 20,
    "page_size": 25,
    "type": "image"
}

response = requests.get(BASE_URL, headers=headers, params=params,verify=False)
print(response.status_code)
file = open("response.txt", "w")
file.write(response.text)
file.close()
