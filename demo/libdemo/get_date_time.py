import requests

resp = requests.get("http://worldtimeapi.org/api/timezone/Asia/Kolkata")
print(resp.status_code)
details = resp.json()   # convert json to dict

print(details['datetime'])
