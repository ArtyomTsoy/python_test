import requests
import os

for i in range(10):
    folder = f'folder_{i}'
    if not os.path.exists(folder):
        os.makedirs(folder)

for i in range(10):
    folder = f'folder_{i}'
    url = requests.get('https://source.unsplash.com/random')
    with open(os.path.join(folder, f'{i}.jpg'), 'wb') as file:
        file.write(url.content)
        print(i, folder)