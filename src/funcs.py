import json


def unpucking_json(file):
    with open(file, 'r', encoding="utf8") as f:
        json_data = f.read()
        data = json.loads(json_data)
        return data





