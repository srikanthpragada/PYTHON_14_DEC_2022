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
        if not href.startswith("/"):
            href = "/" + href

        href = HOST + href

    hrefs.add(href)

print("\nBorken Links\n")

for href in hrefs:
    try:
        # make a request to check health of url
        resp = requests.get(href)
        if resp.status_code != 200:
            print(href)
    except:
        print(href)


