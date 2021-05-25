import json
from pathlib import Path
import csv
import requests

#label_url = ''
#data = requests.get(label_url).json()

with open('label.json') as json_file:
    data = json.load(json_file)

body = data['issue']['body'].split('\r\n')
name = body[0].replace('**Name:** ', '')
email = body[1].replace('**Email:** ', '')
linkedin = body[2].replace('**Linkedin Profile:** ', '')

dict = [{'name': name, 'email': email, 'linkedin': linkedin}]

if not Path('label.csv').is_file():
    with open('label.csv', 'w', newline='') as csv_file:
        columns = ['name', 'email', 'linkedin']
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        writer.writeheader()

with open('label.csv', 'a', newline='') as csv_file:
    columns = ['name', 'email', 'linkedin']
    writer = csv.DictWriter(csv_file, fieldnames=columns)
    writer.writerows(dict)
