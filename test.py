import requests

MAX_REQUESTS = 1000
data = {}
for i in range(MAX_REQUESTS):
    res = requests.get('http://127.0.0.1/api/v1/news/counter/')
    id_ = res.json()['id']
    if data.get(id_):
        data[id_] += 1
    else:
        data[id_] = 1

print(data)