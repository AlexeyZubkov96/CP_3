from cp_3.main import main


def test_main():
    assert main() == f"15.07.2019 Открытие вклада->Счет - **2265\n92688.46USD\n\n" \
                     f"13.07.2019 Перевод с карты на счет\nMaestro - 1308 79** **** 7170->Счет - **8612\n97853.86руб.\n\n" \
                     f"19.05.2019 Перевод организации\nМИР - 5211 27** **** 8469->Счет - **2662\n6381.58USD\n\n" \
                     f"05.01.2019 Перевод со счета на счет\nСчет - **8409->Счет - **8266\n87941.37руб.\n\n" \
                     f"09.03.2018 Перевод организации\nСчет - **3262->Счет - **1315\n25780.71руб.\n\n"
