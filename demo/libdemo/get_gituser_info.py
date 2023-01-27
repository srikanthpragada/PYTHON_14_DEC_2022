import requests

resp = requests.get("https://api.github.com/users/srikanthpragada")
if resp.status_code != 200:
    print("Sorry! Could not get details")
    exit(1)

details = resp.json()   # convert json to dict
print(details['name'])
print(details['company'])
print(details['location'])
