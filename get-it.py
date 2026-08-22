import requests
from bs4 import BeautifulSoup
from requests.models import Response

url = "https://lbsdbearcatcafe.com/index.php?sid=2207151448241738&page=menus"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (64.0.0.0) Safari/537.36"
}

# heading = soup.find("h1")

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Succesfully got page")
        soup = BeautifulSoup(response.text, "html.parser")
        heading = soup.find("h1")
        page_title = heading.get_text(strip=True) if heading else "No Title Found"
        print(f"Page Title: {page_title}")
        print("\nLinks found on page:")
        for link in soup.find_all("a"):
            link_href = link.get("href")
            link_text = link.text.strip()
            print(f"- {link_text}: {link_href}")

    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")
except Exception as e:
    print(f"An error occured: {e}")
