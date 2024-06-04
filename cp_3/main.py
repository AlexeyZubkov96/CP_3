from cp_3.utils import reading_file_json, correct_dictionary, completed_operations, last_five_operations, sorting_by_date
from cp_3.config import PATH_OPERATIONS


def main():
    count_operations_user = int(input("Укажите нужное колличство последних выполненых операций: \n"))
    file_json_convert = reading_file_json(PATH_OPERATIONS)
    execute_operations = completed_operations(file_json_convert)
    sorted_date = sorting_by_date(execute_operations)
    five_execute_operations = last_five_operations(sorted_date, count_operations_user)
    correct_print = correct_dictionary(five_execute_operations)
    result = ""
    for cor in correct_print:
        date_ = cor["date"]
        operation = cor["operation"]
        amount = cor["amount"]
        currency = cor["currency"]
        score_to = cor["score to"]
        if cor.get("from") is None:
            result += f"{date_} {operation}->{score_to}\n{amount}{currency}\n\n"
        else:
            result += f"{date_} {operation}\n{cor['from']}->{score_to}\n{amount}{currency}\n\n"
    return result


if __name__ == "__main__":
    print(main())
