from cp_3.utils import reading_file_json, correct_dictionary, completed_operations, last_five_operations, sorting_by_date, date_formation
from cp_3.config import PATH_OPERATIONS, count_operations


def main():
    file_json_convert = reading_file_json(PATH_OPERATIONS)
    execute_operations = completed_operations(file_json_convert)
    five_execute_operations = last_five_operations(execute_operations, count_operations)
    sorted_date = sorting_by_date(five_execute_operations)
    correct_print = correct_dictionary(sorted_date)
    for cor in correct_print:
        date_ = cor["date"]
        operation = cor["operation"]
        amount = cor["amount"]
        currency = cor["currency"]
        score_to = cor["score to"]
        if cor.get("from") is None:
            print(f"{date_} {operation}"
                  f"->{score_to}\n"
                  f"{amount}{currency}\n")
        else:
            print(f"{date_} {operation}\n"
                  f"{cor['from']}->{score_to}\n"
                  f"{amount}{currency}\n")


if __name__ == "__main__":
    main()
