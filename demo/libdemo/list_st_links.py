import requests
from bs4 import BeautifulSoup

HOST = "http://www.srikanthtechnologies.com"
resp = requests.get(HOST)
bs = BeautifulSoup(resp.text, 'html.parser')

links = bs.find_all("a")
hrefs = set()
for link in links:
    href = link['href']
    if href == '#':
        continue

    if not href.startswith("http"):
          href= HOST + "/" + href

    hrefs.add(href)

for href in hrefs:
    print(href)

print(f"\nCount = {len(hrefs)}")



