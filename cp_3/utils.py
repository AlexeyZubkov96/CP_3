import json

from config import PATH_OPERATIONS


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
