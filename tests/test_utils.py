from cp_3.utils import hiding_account


def test_hiding_account():
    assert hiding_account("Счет 18889008294666828266") == "**8266"


