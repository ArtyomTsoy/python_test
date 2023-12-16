import requests
import json

url = 'https://jsonplaceholder.typicode.com/todos/'

response = requests.get(url)
if response.status_code == 200:
    tasks = response.json()

    with open('output.json', 'w') as file:
        json.dump(tasks, file, indent=4)

with open('output.json', 'r') as file:
    tasks = json.load(file)

print(tasks[:2])

for index, task in enumerate(tasks):
    name = f'todo_index.json'
    with open('name', 'w') as individual_file:
        json.dump(task, individual_file, indent=4)