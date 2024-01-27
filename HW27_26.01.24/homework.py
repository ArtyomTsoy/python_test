import requests
import os

a = 'files'
os.makedirs(a, exist_ok=True)
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
data = response.json()

for index, item in enumerate(data):
    output = os.path.join(a, f'{index}.json')
    with open(output, 'w') as file:
        file.write(str(item))

print(a)