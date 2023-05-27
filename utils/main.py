from utils.funcs import sorted_operacions, format_date, format_card, format_score

operacions = sorted_operacions(5)

for operacion in operacions:
    """ Перебираем операции, выводим информацию в зависимости от условии"""
    currency = operacion["operationAmount"]["currency"]["name"]
    print(f'{format_date(operacion["date"])} {operacion["description"]}')
    if "from" in operacion:
        if operacion["description"] == "Перевод с карты на карту":
            print(f'{format_card(operacion["from"])} -> {format_card(operacion["to"])}')
            print(f'{operacion["operationAmount"]["amount"]} {currency}\n')
        elif operacion["description"] == "Перевод организации":
            print(f'{format_card(operacion["from"])} -> {format_score(operacion["to"])}')
            print(f'{operacion["operationAmount"]["amount"]} {currency}\n')
        elif operacion["description"] == "Перевод со счета на счет":
            print(f'{format_score(operacion["from"])} -> {format_score(operacion["to"])}')
            print(f'{operacion["operationAmount"]["amount"]} {currency}\n')
    else:
        print(f'{format_score(operacion["to"])}')
        print(f'{operacion["operationAmount"]["amount"]} {currency}\n')
