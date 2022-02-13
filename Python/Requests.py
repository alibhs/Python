import requests
import json

site = requests.get("https://jsonplaceholder.typicode.com/todos")
cevap = json.loads(site.text)
# print(cevap[0])
# print(cevap[0]["title"])
for i in cevap:
    print(i["title"])