import json


def unpucking_json(file):
    with open(file, 'r', encoding="utf8") as f:
        json_data = f.read()
        data = json.loads(json_data)
        return data


def cleaning_data(data):
    new_data = []
    for transaction in data:
        if not transaction:
            continue
        elif transaction['state'] == 'CANCELED':
            continue
        else:
            new_data.append(transaction)
    return new_data
