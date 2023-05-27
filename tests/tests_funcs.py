from utils.funcs import format_date, format_card, format_score


def test_format_date():
    assert format_date("2018-04-04T17:33:34.701093") == "04.04.2018"


def test_format_card():
    assert format_card("Visa Gold 5999414228426353") == "Visa Gold 5999 42** **** 6353"
    assert format_card("MasterCard 7158300734726758") == "MasterCard 7158 07** **** 6758"


def test_format_score():
    assert format_score("Счет 72731966109147704472") == "Счет **4472"
