import requests
from bs4 import BeautifulSoup

HOST = "https://www.w3schools.com"
resp = requests.get(HOST)
bs = BeautifulSoup(resp.text, 'html.parser')

links = bs.find_all("a")
hrefs = set()
for link in links:
    href = link['href']
    if href == '#':
        continue

    if not href.startswith("http"):
        if not href.startswith("/"):
            href = "/" + href

        href = HOST + href

    hrefs.add(href)

for href in hrefs:
    print(href)

print(f"\nCount = {len(hrefs)}")
