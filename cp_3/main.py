from utils import correct_dictionary


def main():
    correct = correct_dictionary()
    for cor in correct:
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
