import pytest
from mywork.src.utils import func_user_currencies, func_user_stocks

def test_func_user_currencies():
    '''тест для функции которая достает из файла данные о 'пользовательских настройках' для курса валют'''
    user_currencies = func_user_currencies()
    assert user_currencies == ['USD', 'EUR']


def test_func_user_stocks():
    '''тест для функции которая достает из файла данные о 'пользовательских настройках' для стоимости акций'''
    user_stocks = func_user_stocks()
    assert user_stocks == ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA']