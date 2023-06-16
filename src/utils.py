from json import load


def load_list_with_operations(file: str) -> [str, list]:
    """Получаем список всех операций"""
    # проверка на корректность файла
    if not file.endswith('.json'):
        return 'Неверный формат файла'
    with open(file=file) as file:
        list_with_operations = load(file)

    return list_with_operations


def sorted_list_with_operations(list_with_operations):
    """Получаем 5 последних операций и сортируем их по дате. От самых новых к самым старым"""
    # Список куда будем всё складывать
    sorted_list = []
    # Проходим по циклу
    for operation in list_with_operations:
        # проверка на пустую операцию
        if operation:
            # проверка на подтверждение операции
            if operation['state'] == 'EXECUTED':
                # проверка на перевод организации
                if operation['description'] == 'Перевод организации':
                    # убираем перевод со счета на счет, потому что они не подходят под формат вывода(4 блока по 4 цифры)
                    if operation['from'].startswith('Счет'):
                        continue
                    # убираем старые операции
                    if operation['date'].startswith('2018'):
                        continue
                    # делаем сразу удобный для нас вывод времени и даты
                    operation['date'] = operation['date'][8:10] + '.' + operation['date'][5:7] + '.' + operation['date'][:4]
                    # добавляем в список
                    sorted_list.append(operation)

    # сортировка по месяцам
    sorted_list.sort(key=lambda a: a['date'][3:5], reverse=True)
    # сортировка по числам и месяцам
    for index in range(len(sorted_list) - 1):
        # если дата одной операции меньше другой и месяца одинаковые - меняем их местами, так как по месяцам уже отсортировал
        if sorted_list[index]['date'][0:2] < sorted_list[index + 1]['date'][0:2] and sorted_list[index]['date'][3:5] == sorted_list[index + 1]['date'][3:5]:
            sorted_list[index], sorted_list[index + 1] = sorted_list[index + 1], sorted_list[index]
    # возвращаем только первые 5 операций срезом
    return sorted_list[:5]


def main(completed_list):
    """Функция основная, выводит итоговые результаты"""
    # создаю словарь, куда буду складывать сразу форматированную информацию о переводе
    dict_with_info_to_message = {
        'date': None,
        'amount_with_name': None,
        'description': None,
        'from': None,
        'to': None

    }
    # бегу по списку операций циклом
    for operation in completed_list:
        # дата
        dict_with_info_to_message['date'] = operation['date']
        # описание операции
        dict_with_info_to_message['description'] = operation['description']
        # сумма перевода + валюта
        dict_with_info_to_message['amount_with_name'] = str(operation['operationAmount']['amount']) + ' ' + str(operation['operationAmount']['currency']['name'])
        # срезом получаю последние 4 цифры счета
        dict_with_info_to_message['to'] = 'Счет ' + '**' + operation['to'][-4:]
        # тут корячусь но получаю нужный нам формат для вывода
        dict_with_info_to_message['from'] = operation['from'][:-16] + operation['from'][-16:-12] + ' ' + operation['from'][-12:-10] + '**' + ' **** ' + operation['from'][-4:]
        # сам вывод в нужном нам формате
        print(f"{dict_with_info_to_message['date']} {dict_with_info_to_message['description']}\n"
              f"{dict_with_info_to_message['from']} -> {dict_with_info_to_message['to']}\n"
              f"{dict_with_info_to_message['amount_with_name']}")
        # пустая строка для разделения операция на выводе
        print()


if __name__ == '__main__':
    main(sorted_list_with_operations(load_list_with_operations('operations.json')))
