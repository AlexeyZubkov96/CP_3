import json

from datetime import datetime


def reading_file_json(operations):
    """
    Чтение файла формата .json
    """
    with open(operations, "r", encoding="utf-8") as file:
        file_json = json.loads(file.read())
        return file_json


def completed_operations(operations_list):
    """
    Возвращает список всех выполненых операций
    """
    list_completed_operations = []
    for opera in operations_list:
        if opera.get("state") is None:
            continue
        elif opera["state"] == "EXECUTED":
            list_completed_operations.append(opera)
    return list_completed_operations


def last_five_operations(operations, count_operations):
    """
    Возвращает список словарей последних выполненых операций взависимости от требуемого количества
    """
    five_operations = operations[-count_operations::]
    return five_operations


def sorting_by_date(five_operations):
    """
    Возвращает отсортированный список по дате
    """
    sorted_date_operations = sorted(five_operations, key=lambda x: x['date'], reverse=True)
    return sorted_date_operations


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


def correct_dictionary(five_operations):
    """
    Возвращает список словарей с обработаными данными
    """
    user_print_list = []
    for opera in five_operations:
        user_print_dict = {}
        rus_date = date_formation(opera["date"])
        user_print_dict["date"] = rus_date
        operation_type = opera["description"]
        user_print_dict["operation"] = operation_type
        amount_user = opera["operationAmount"]["amount"]
        user_print_dict["amount"] = amount_user
        currency = opera["operationAmount"]["currency"]["name"]
        user_print_dict["currency"] = currency
        if opera.get("from") is None:
            if opera["to"].count("Счет") >= 1:
                user_print_dict["score to"] = hiding_account(opera["to"])
            else:
                user_print_dict["score to"] = hiding_card(opera["to"])
                continue
        elif opera["from"].count("Счет") >= 1:
            account = hiding_account(opera["from"])
            user_print_dict["from"] = account
            if opera["to"].count("Счет") >= 1:
                user_print_dict["score to"] = hiding_account(opera["to"])
            else:
                user_print_dict["score to"] = hiding_card(opera["to"])
        else:
            card = hiding_card(opera["from"])
            user_print_dict["from"] = card
            if opera["to"].count("Счет") >= 1:
                user_print_dict["score to"] = hiding_account(opera["to"])
            else:
                user_print_dict["score to"] = hiding_card(opera["to"])
        user_print_list.append(user_print_dict)
    return user_print_list


