import json
from data.config import PATH_COMPANY

with open(PATH_COMPANY, 'r', encoding='UTF-8') as f:
    data = json.load(f)
    for name, id in data.items():
        print(name, id)

