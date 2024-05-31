import json

from config import PATH_OPERATIONS
from datetime import datetime


def reading_file_json(operations):
    """
    Чтение файла формата .json
    """
    with open(operations, "r", encoding="utf-8") as file:
        file_json = json.loads(file.read())
        return file_json


def completed_operations():
    """
    Возвращает список всех выполненых операций
    """
    operations_list = reading_file_json(PATH_OPERATIONS)
    list_completed_operations = []
    for opera in operations_list:
        if opera.get("state") is None:
            continue
        elif opera["state"] == "EXECUTED":
            list_completed_operations.append(opera)
    return list_completed_operations


def last_five_operations():
    """
    Возвращает список словарей пяти последних выполненых операций
    """
    operations = completed_operations()
    five_operations = operations[-5::]
    return five_operations


def date_formation(date):
    """
    Возвращает дату в формате(ДД.ММ.ГГ)
    """
    date_ = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return f'{date_:%d.%m.%Y}'


def hiding_card(card):
    """
    Возвращает номер карты в формате ХХХХ ХХ** **** XXXX
    """
    split_str_score = card.split(" ")
    card_number = "".join(split_str_score[-1])
    name_card = " ".join(split_str_score[:-1])
    private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
    return f"{name_card} - {private_number[:4]} {private_number[4:8]} {private_number[8:12]} {private_number[12:]}"


def hiding_account(account):
    """
    Возвращает номер счета в формате **XXXX
    """
    split_str_account = account.split(" ")
    account_number = "".join(split_str_account[-1])
    name_account = " ".join(split_str_account[:-1])
    last_six_digits = account_number[-6:]
    hiding = len(last_six_digits[:2]) * "*" + last_six_digits[2:]
    return f"{name_account} - {hiding}"

print(hiding_card("Visa 3654412434951162"))
print(hiding_account("Счет 59986621134048778289"))
