import json
import pathlib
from pathlib import Path
import csv

import requests

#label_url = ''
#data = requests.get(label_url).json()

with open('label.json') as json_file:
    data = json.load(json_file)

name = 'Vaya Pupkin'
email = 'vasya@pupkin.com'
linkedin = 'https://linkedin.com/in/vasyapupkin'

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
