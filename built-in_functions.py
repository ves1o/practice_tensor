from typing import Tuple, List, Dict, Callable, Any
import functools
import time
import re
import os


#7
def func_time(func: Callable) -> Callable:
    """
    Декоратор, вычисляющий вресмя работы функции
    :param func: какая-то функция
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        total_time = end - start
        print(f'Функция {func.__name__} выполнялась {total_time:.4f} сек')
        return result

    return wrapped_func


def a_hater(text: str) -> Tuple[str, int]:
    """
    Функция убирает все буквы А из строки и подсчитывает их количество
    :param text: любая строка
    """

    a_counter = 0
    result = ''
    prev_a = 0
    for index, symbol in enumerate(text):
        if symbol in ['A', 'a']:
            result += text[prev_a:index]
            prev_a = index + 1
            a_counter += 1
    result += text[prev_a:]
    return result, a_counter


def is_phone_number(text: str) -> bool:
    """
    Проверка соответствия патерну номера телефона
    :param text: любая строка
    :return: bool
    """

    phone_number_pattern = re.compile(r'^\+?\d([ -]?\d{3}){2}[ -]?\d{2}[ -]?\d{2}$')
    if phone_number_pattern.match(text):
        return True
    return False


def file_name(path: str) -> str:
    """
    получение имени файла без расширения
    :param path: путь до файла
    """

    directories = path.split(os.sep)
    file = directories[-1].split('.')[:-1]
    name = '.'.join(file)
    return name


def max_min_change(elements: List) -> List:
    """
    меняет местами минимальный и максимальный элемент списка
    :param elements: список из чисел, либо строк
    """

    maximum = max(elements)
    minimum = min(elements)
    elements[elements.index(maximum)], elements[elements.index(minimum)] = minimum, maximum
    return elements


def two_most_expensive_products(products: List[Dict]) -> List[Dict]:
    """
    Нахождение самых дорогих товаров из списка
    :param products: pсписок словарей с ключами "наименование" и "цена"
    :return: список из двух самых дорогих товаров
    """

    products_by_price = dict()
    for product in products:
        if product['цена'] in products_by_price.keys():
            products_by_price[product['цена']].append(product)
        else:
            products_by_price[product['цена']] = [product]
    sorted_prices = sorted(products_by_price.keys(), reverse=True)
    if len(products_by_price[sorted_prices[0]]) > 1:
        return products_by_price[sorted_prices[0]][:2]
    return [products_by_price[sorted_prices[0]][0], products_by_price[sorted_prices[1]][0]]


def digit_sum(number: int) -> int:
    """
    сумма цифр числа не больше 3х знаков
    :param number: число неболее трехзнаков
    """
    if number > 999:
        raise ValueError('число имеет больше 3х знаков')

    last_digit = number % 10
    first_digit = number // 100
    if number // 10 > 9:
        middle_digit = number // 10 % 10
    else:
        middle_digit = number // 10
    return last_digit + middle_digit + first_digit


@func_time
def happy_ticket_counter() -> int:
    """
    подсчитывает количество "счастливых" билетиков
    :return: целое число
    """

    counter = 1
    for left_part in range(1, 1000):
        for right_part in range(1, 1000):
            if digit_sum(left_part) == digit_sum(right_part):
                counter += 1
    return counter


if __name__ == '__main__':
    #1
    print(a_hater('abcdAbc'))

    #2
    phones_data = ['8-999-777-1111', '+7 999 333 2222', '+7 a99-555-11-11']
    test_phones_data = [True, True, False]

    for elem, res in zip(phones_data, test_phones_data):
        assert is_phone_number(elem) == res

    #3
    print(file_name(r'C:\development\inside\test-project_management\inside\my.file.txt'))

    #4
    test = [1, 2, 4, -2, 2, 6, 7, 0, 12]
    print(max_min_change(test))

    #5
    products_data = [{'наименование': 'Спички', 'цена': 1400}, {'наименование': 'Лук', 'цена': 137},
                     {'наименование': 'пирог', 'цена': 140},  {'наименование': 'топор', 'цена': 137}]
    print(two_most_expensive_products(products_data))

    #6
    print(happy_ticket_counter())
