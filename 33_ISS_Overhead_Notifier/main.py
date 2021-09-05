import requests


response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status():
print(response.json()["iss_position"])
