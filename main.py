from functions import *


def main():
    URL = "https://www.jsonkeeper.com/b/CNBC"
    IGNORE_INCOMPLETE_TRANSACTIONS = True

    data = get_data(URL)
    data = formatted_data_by_time(data)
    data = get_from(data, ignore_incomplete_transactions=IGNORE_INCOMPLETE_TRANSACTIONS)
    data = get_right_data(data)

    print()
    for i in data:
        print(i)


if __name__ == "__main__":
    main()
