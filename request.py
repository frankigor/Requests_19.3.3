import requests

url_1 = 'https://petstore.swagger.io/v2/pet/findByStatus/'
url_2 = 'https://petstore.swagger.io/v2/pet/'
headers = {'accept': 'application/json'}
data = {
        "id": 12,
        "category": {
            "id": 25,
            "name": "dog"
        },
        "name": "DogTest",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 14,
                "name": "string"
            }
            ],
        "status": "available"
    }

data_1 = {
        "id": 12,
        "category": {
            "id": 25,
            "name": "cat"
        },
        "name": "CatTest",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 14,
                "name": "string"
            }
        ],
        "status": "available"
    }


res = requests.get(url_1, params={'status': 'available'}, headers=headers)
print(res.status_code)
if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)

res = requests.post(url_2, headers=headers, json=data)
print(res.status_code)
if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)

res = requests.put(url_2, json=data_1)
print(res.status_code)
if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)

res = requests.delete(url_2+str(res.json()['id']))
print(res.status_code)
if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)
