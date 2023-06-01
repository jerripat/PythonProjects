import requests
import json

response = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

data = json.loads(response.text)

for i in range(len(data['items'])):

    print(data['items'][i]['title'])