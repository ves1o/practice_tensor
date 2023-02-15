import os
from typing import List


def files_in_directory(path: str) -> List[str]:
    """
    Находит все файлы в директории
    :param path: путь до директории
    :return: список файлов
    """
    result = list()
    for element in os.listdir(path):
        element_path = os.path.join(path, element)
        if os.path.isfile(element_path):
            result.append(element)
    return result


def dir_file_path(directory: str, file: str) -> str:
    """
    ОбЬединяет путь до директории и файл
    :param directory: путь до директории
    :param file: имя файла
    :return: путь до файла в директории
    """
    return os.path.join(directory, file)


def directory_stat(path: str) -> List[int]:
    """
    Подсчет количесвта директорий, .py файлов, .exe файлов и общего количества файлов в директории
    :param path: путь до директории
    :return: список целых чисел
    """
    # [кол-во папок, кол-во ".py", кол-во ".exe", всего файлов]
    result = [0, 0, 0, 0]

    for element in os.listdir(path):
        element_path = os.path.join(path, element)
        if os.path.isfile(element_path):
            result[3] += 1
            if element[-3:] == '.py':
                result[1] += 1
            elif element[-4:] == '.exe':
                result[2] += 1
        else:
            result[0] += 1
            dir_stat = directory_stat(element_path)
            result[0] += dir_stat[0]
            result[1] += dir_stat[1]
            result[2] += dir_stat[2]
            result[3] += dir_stat[3]

    return result


if __name__ == '__main__':

    #1
    root = os.path.abspath(os.sep)
    print(files_in_directory(os.path.join(root, 'Users\dk.loshkin\Documents')))

    #2
    current_dir = os.getcwd()
    print(current_dir)

    #3
    os.mkdir(os.path.join(current_dir, 'test_dir'))

    #4
    dir = 'dk.loshkin\Documents'
    file_name = 'test.txt'
    print(dir_file_path(dir, file_name))

    #5
    python_dir = os.path.abspath('C:\Program Files (x86)\Python38-32')
    with open('dir_stat.txt', 'w', encoding='utf-8') as file_stat:
        python_dir_stat = directory_stat(python_dir)
        file_stat.write(f'Папок: {python_dir_stat[0]}\n'
                        f'файлов ".py": {python_dir_stat[1]}\n'
                        f'файлов ".exe": {python_dir_stat[2]}\n'
                        f'всего файлов: {python_dir_stat[3]}')

