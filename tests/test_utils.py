from cp_3.utils import hiding_account, completed_operations, last_five_operations, sorting_by_date, date_formation, hiding_card, correct_dictionary


def test_completed_operations():
    operations_all = [
        {"state": "EXECUTED", "date": "11.02.2023"},
        {"state": "CANCELED"},
        {},
        {"state": "test"},
        {"state": "EXECUTED", "date": "12.03.2019"}
    ]
    operations_executed = [
        {"state": "EXECUTED", "date": "11.02.2023"},
        {"state": "EXECUTED", "date": "12.03.2019"}
    ]
    assert completed_operations(operations_all) == operations_executed


def test_hiding_account():
    assert hiding_account("Счет 18889008294666828266") == "Счет - **8266"


def test_last_five_operations():
    operations_all = [
        {"state": "EXECUTED", "date": "11.02.2023"},
        {"state": "CANCELED"},
        {},
        {"state": "test"},
        {"state": "EXECUTED", "date": "12.03.2019"},]
    operations_last = [
        {"state": "test"},
        {"state": "EXECUTED", "date": "12.03.2019"},
    ]
    assert last_five_operations(operations_all, 2) == operations_last


def test_sorting_by_date():
    data_no_sort = [
        {"date": "2019-01-05T00:52:30.108534"},
        {"date": "2019-07-13T18:51:29.313309"}]
    data_sort = [
        {"date": "2019-07-13T18:51:29.313309"},
        {"date": "2019-01-05T00:52:30.108534"}]
    assert sorting_by_date(data_no_sort) == data_sort


def test_date_formation():
    assert date_formation("2019-01-05T00:52:30.108534") == "05.01.2019"


def test_hiding_card():
    assert hiding_card("МИР 5211277418228469") == "МИР - 5211 27** **** 8469"


def test_correct_dictionary():
    operation_before = [{'id': 207126257,
                         'state': 'EXECUTED',
                         'date': '2019-07-15T11:47:40.496961',
                         'operationAmount': {'amount': '92688.46',
                                             'currency': {'name': 'USD', 'code': 'USD'}},
                         'description': 'Открытие вклада',
                         'to': 'Счет 35737585785074382265'}]
    operation_after = [
        {
            "date": "15.07.2019",
            "operation": 'Открытие вклада',
            "amount": '92688.46',
            "currency": 'USD',
            "score to": 'Счет - **2265'}
    ]
    assert correct_dictionary(operation_before) == operation_after
