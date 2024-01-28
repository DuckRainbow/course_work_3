import json
from datetime import datetime


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


def date_form(date_in):
    date_out = datetime.strftime(datetime.strptime(date_in.split('T')[0], '%Y-%m-%d'), '%d.%m.%Y')
    return date_out


def reformating_num(bill_or_card):
    data_trnsctn = bill_or_card.split(" ")
    bill_or_card_name = ' '.join([element for element in data_trnsctn if not element.isdigit()])
    bill_or_card_num = data_trnsctn[-1]
    if data_trnsctn[0] == 'Счет':
        return bill_or_card_name + ' **' + bill_or_card_num[-4:]
    return bill_or_card_name + ' ' + bill_or_card_num[:4] + ' ' + bill_or_card_num[
                                                                  4:6] + '** ' + '**** ' + bill_or_card_num[-4:]


def outputting_data(some_dict):
    return (f"{date_form(some_dict['date'])}, {some_dict['description']}\n"
            f"{some_dict.get('from')} -> {some_dict['to']}\n"
            f"{some_dict['operationAmount']['amount']} {some_dict['operationAmount']['currency']['name']} \n")
