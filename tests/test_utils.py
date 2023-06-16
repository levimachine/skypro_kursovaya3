from src.utils import load_list_with_operations, sorted_list_with_operations, main
import pytest


def test_load_list_with_operations():
    assert load_list_with_operations('test.txt') == 'Неверный формат файла'
    assert load_list_with_operations('testing.json') == [
        {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
         "description": "Перевод организации", "from": "MasterCard 7158300734726758", "to": "Счет 35383033474447895560"}]


def test_sorted_list_with_operations():
    with pytest.raises(TypeError):
        sorted_list_with_operations(123)
    assert sorted_list_with_operations(
        [{'id': 179194306, 'state': 'EXECUTED', 'date': '2019-05-19T12:51:49.023880', 'operationAmount': {'amount': '6381.58', 'currency': {'name': 'USD', 'code': 'USD'}},
          'description': 'Перевод организации', 'from': 'МИР 5211277418228469', 'to': 'Счет 58518872592028002662'}
         ]) == [{'id': 179194306, 'state': 'EXECUTED', 'date': '19.05.2019', 'operationAmount': {'amount': '6381.58', 'currency': {'name': 'USD', 'code': 'USD'}},
                 'description': 'Перевод организации', 'from': 'МИР 5211277418228469', 'to': 'Счет 58518872592028002662'}]


def test_main():
    with pytest.raises(TypeError):
        main(123)
    with pytest.raises(TypeError):
        main([{'id': 441945886, 'state': 'EXECUTED', 'date': '123', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 123}])
    with pytest.raises(TypeError):
        main([{'id': 441945886, 'state': 'EXECUTED', 'date': '123', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 123}])
    with pytest.raises(TypeError):
        main([{'id': 441945886, 'state': 'EXECUTED', 'date': '123', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Перевод организации', 'from': 123, 'to': 'Счет 64686473678894779589'}])
    main([{'id': 441945886, 'state': 'EXECUTED', 'date': '123', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
           'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}])
