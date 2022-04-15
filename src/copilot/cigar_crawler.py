from googlesearch import search
import requests

locationStr = "cigars ziggaren near 51.9716646,7.610422"
results = search(locationStr, lang="en")

for result in results:
    print(result)
    r = requests.get(result)
    print(r.status_code)
