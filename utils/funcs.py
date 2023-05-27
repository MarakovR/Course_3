import json
import os.path


def open_file():
    """ Возвращает содержимое файла json """
    file = open("/home/roman/PycharmProjects/Course_3/files/operations.json")
    json_file = json.load(file)
    operations_file = [i for i in json_file if i]
    return operations_file


def sorted_operacions(value):
    """ Находим последние выполненные операции по ключам 'date' и 'state' """
    operacions = sorted(open_file(), key=lambda x: x["date"], reverse=True)[:value]
    operacions_exe = []
    for operacion in operacions:
        if operacion["state"] == "EXECUTED":
            operacions_exe.append(operacion)
        else:
            continue
    return operacions_exe


def format_date(date):
    """ Меняем формат даты """
    day = date[8:10]
    month = date[5:7]
    yar = date[0:4]
    return f"{day}.{month}.{yar}"


def format_card(card):
    """ Меняем формат карты """
    name_card = card[:-16]
    number_card = card[-16:]
    number_1 = number_card[:4]
    number_2 = number_card[4:8]
    number_2 = number_2[2:] + "**"
    number_3 = "****"
    number_4 = number_card[12:16]
    number_card = f'{number_1} {number_2} {number_3} {number_4}'
    name_numder_card = name_card + number_card
    return name_numder_card


def format_score(score):
    """ Меняем формат счета """
    number_score = score[-20:]
    number_score = "**" + number_score[-4:]
    name_score = score[:-20]
    name_number_score = name_score + number_score
    return name_number_score
