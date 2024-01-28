import json
from datetime import datetime
from funcs import unpucking_json, cleaning_data, date_form, outputting_data


def main_func():
    data_ = unpucking_json('operations.json')
    cleaned_data = cleaning_data(data_)

    sorted_data = sorted(cleaned_data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)

    time = 0
    for trns in sorted_data:
        time += 1
        print(outputting_data(trns))
        if time == 5:
            break


if __name__ == "__main__":
    main_func()
