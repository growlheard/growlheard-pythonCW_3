from datetime import datetime


import requests


def get_data(url):
    results = requests.get(url)
    return results.json()


def formatted_data_by_time(data):
    format_date = []
    for i in range(len(data)):
        if "state" not in data[i]:
            continue
        if data[i]["state"] == "EXECUTED":
            format_date.append(data[i])
    format_date.sort(key=lambda dates: dates["date"], reverse=True)
    return format_date


def get_from(data, ignore_incomplete_transactions=False):
    if ignore_incomplete_transactions:
        data = [x for x in data if "from" in x]
        return data[:5]


def get_right_data(data):
    formatted_date = []
    for i in data:
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = i["description"]
        from_ = i["from"].split()
        bill_number = from_.pop(-1)
        bill_number = f"{bill_number[:4]} {bill_number[4:6]}** *** {bill_number[-4:]}"
        info = " ".join(from_)
        to = f"{i['to'].split()[0]} **{i['to'][-4:]}"
        operation_amount = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"

        formatted_date.append(f"""\n{date} {description}\n{info} {bill_number} -> {to}\n{operation_amount}\n""")

    return formatted_date
