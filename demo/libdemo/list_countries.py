import requests

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print("Sorry! Could not get details")
    exit(1)

countries = resp.json()  # convert array of json to list of dict

for country in sorted(countries,
                      key=lambda c: c['population'],
                      reverse=True)[:10]:
    name = country['name']["common"]
    population = country["population"]
    print(f"{name:50} {population:12}")
