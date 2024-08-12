import json
from typing import Any, Hashable

import pandas as pd


def read_excel(path: str) -> list[dict[Hashable, Any]]:
    """считывает финансовые операции с файла excel"""

    excel_file = pd.read_excel(path)

    return excel_file.to_dict(orient="records")


# print(read_excel('../data/operations.xls'))


def func_user_currencies():
    with open('../user_settings.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data['user_currencies']

user_currencies = func_user_currencies()

def func_user_stocks():
    with open('../user_settings.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data['user_stocks']

user_stocks = func_user_stocks()
