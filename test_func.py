from functions import *


def test_get_data_success():
    assert len(get_data("https://www.jsonkeeper.com/b/CNBC")[0]) > 0


def test_formatted_data_by_time():
    data = [
        {"state": "EXECUTED", "date": "2022-12-01"},
        {"state": "EXECUTED", "date": "2022-11-01"},
        {"state": "CANCELLED", "date": "2022-10-01"},
        {"state": "EXECUTED", "date": "2022-09-01"},
        {"state": "EXECUTED", "date": "2022-08-01"},
    ]
    assert formatted_data_by_time(data) == [
        {"state": "EXECUTED", "date": "2022-12-01"},
        {"state": "EXECUTED", "date": "2022-11-01"},
        {"state": "EXECUTED", "date": "2022-09-01"},
        {"state": "EXECUTED", "date": "2022-08-01"},
    ]


def test_formatted_data_by_time_with_empty_data():
    data = []
    assert formatted_data_by_time(data) == []


def test_formatted_data_by_time_with_no_executed_data():
    data = [
        {"state": "CANCELLED", "date": "2022-10-01"},
        {"state": "CANCELLED", "date": "2022-09-01"},
    ]
    assert formatted_data_by_time(data) == []


def test_get_from_without_incomplete_transactions():
    data = [{"from": "A", "amount": 10},
            {"to": "B", "amount": 20},
            {"from": "C", "amount": 30},
            {"from": "D", "amount": 40},
            {"from": "E", "amount": 50},
            {"to": "F", "amount": 60}]

    assert get_from(data, ignore_incomplete_transactions=True) == [{"from": "A", "amount": 10},
                                                                   {"from": "C", "amount": 30},
                                                                   {"from": "D", "amount": 40},
                                                                   {"from": "E", "amount": 50}]
def test_get_right_data_with_valid_data():
    data = [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]
    assert get_right_data(data)== ['\n26.08.2019 Перевод организации\nMaestro 1596 83** *** 5199 -> Счет **9589\n31957.58 руб.\n']

