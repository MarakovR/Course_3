from utils.funcs import format_date, format_card, format_score, sorted_operacions


def test_format_date():
    assert format_date("2018-04-04T17:33:34.701093") == "04.04.2018"


def test_format_card():
    assert format_card("Visa Gold 5999414228426353") == "Visa Gold 5999 42** **** 6353"
    assert format_card("MasterCard 7158300734726758") == "MasterCard 7158 07** **** 6758"


def test_format_score():
    assert format_score("Счет 72731966109147704472") == "Счет **4472"

def test_sorted_operacions():
    assert sorted_operacions(2) == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}]