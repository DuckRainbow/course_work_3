from src.funcs import unpucking_json, cleaning_data, date_form, reformating_num


def test_unpucking_json():
    assert unpucking_json('src/test.json') == {'id': 441945886}


def test_cleaning_data():
    assert cleaning_data([{}, {}]) == []
    assert cleaning_data([{'state': 'CANCELED'}, {}]) == []
    assert cleaning_data([{'state': 'CANCELED'}, {'state': 'EXECUTED'}]) == [{'state': 'EXECUTED'}]


def test_date_form():
    assert date_form('2018-10-14T08:21:33.419441') == '14.10.2018'


def test_reformating_num_card():
    assert reformating_num('Maestro 4598300720424501') == 'Maestro 4598 30** **** 4501'


def test_reformating_num_bill():
    assert reformating_num('Счет 43597928997568165086') == 'Счет **5086'
