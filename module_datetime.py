from datetime import datetime, timedelta


def plus_ten_days(text_date: str) -> str:
    """
    Прибавляет 10 дней к дате
    :param text_date: дата в виде строки 11.01.12
    :return: дата в виде строки 21.01.12
    """
    beautiful_date = datetime.strptime(text_date, "%d.%m.%y") + timedelta(days=10)
    return beautiful_date.strftime("%d.%m.%Y")


def first_day(date: datetime) -> str:
    """
    Первый день месяца
    :param date: дата в формате datetime
    :return: дата в виде строки 01.01.23
    """
    return date.replace(day=1).strftime("%d.%m.%y")


def last_day(date: datetime) -> str:
    """
    Последний день месяца
    :param date: дата в формате datetime
    :return: дата в виде строки 31.01.23
    """
    next_month = date.replace(day=28) + timedelta(days=4)
    result = next_month - timedelta(days=next_month.day)
    return result.strftime("%d.%m.%y")


def plus_month(date: datetime) -> str:
    """
    Прибавляет месяц к дате
    :param date: дата в формате datetime
    :return: дата в виде строки 31.01.2023
    """
    day = date.day
    next_month = date.replace(day=28) + timedelta(days=4)
    result = next_month.replace(day=day)
    return result.strftime("%d.%m.%Y")


def minus_month(date: datetime) -> str:
    """
    Вычитает месяц из даты
    :param date: дата в формате datetime
    :return: дата в виде строки 31.01.2023
    """
    day = date.day
    prev_month = date.replace(day=1) - timedelta(days=1)
    result = prev_month.replace(day=day)
    return result.strftime("%d.%m.%Y")


def change_month(text_date: str, month: int) -> str:
    """
    Прибавляет\вычитает указанное количество месяцев
    :param text_date: дата в виде строки 31.01.23
    :param month: целое число
    :return: дата в виде строки 31.01.23
    """
    beautiful_date = datetime.strptime(text_date, "%d.%m.%y")
    if month == 0:
        result = beautiful_date
    elif month > 0:
        result = beautiful_date
        for _ in range(month):
            result = datetime.strptime(plus_month(result), "%d.%m.%Y")
    else:
        result = beautiful_date
        for _ in range(-month):
            result = datetime.strptime(minus_month(result), "%d.%m.%Y")

    return result.strftime("%d.%m.%y")


if __name__ == '__main__':

    #1
    five_days_feature = datetime.today() + timedelta(days=5)
    print(five_days_feature.strftime("%d.%m.%y"))

    #2
    print(datetime.today().strftime("%d.%m.%Y"))

    #3
    print(plus_ten_days('03.05.13'))

    #4
    print(first_day(datetime.today()))

    #5
    print(last_day(datetime.today()))

    #6
    print(plus_month(datetime.today()))

    #7
    print(change_month('12.12.12', -7))
