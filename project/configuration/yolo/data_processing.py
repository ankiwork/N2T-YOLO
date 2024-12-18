import os
from project.modules.zip import check_and_create_file


# TODO: переделать под работу с json файлом. Поиск осуществлять по ключу.
def save_data(data, file_path):
    """
    Сохраняет данные в файл.

    Параметры:
    Data (str): Данные для сохранения в файл.
    File_path (str): Путь к файлу, в который будут сохранены данные.

    Возвращает:
    None
    """
    # Проверяем и создаем файл, если он не существует
    check_and_create_file(os.path.dirname(file_path), os.path.basename(file_path))

    # Записываем данные в файл
    with open(file_path, "w") as file:
        file.write(data)


# TODO: переделать под работу с json файлом. Поиск осуществлять по ключу.
def load_data(file_path):
    """
    Загружает данные из файла.

    Параметры:
    File_path (str): Путь к файлу для загрузки данных.

    Возвращает:
    Str: Содержимое файла или пустую строку, если файл не существует или пуст.
    """
    try:
        with open(file_path, "r") as file:
            return file.read().strip()

    except FileNotFoundError:
        return ""


# TODO: переделать под работу с json файлом. Поиск осуществлять по ключу.
def handle_data_selection(selected_data, file_path):
    """
    Обрабатывает выбор данных и сохраняет их в файл.

    Параметры:
    Selected_data (str): Выбранные данные для сохранения.
    File_path (str): Путь к файлу для сохранения данных.

    Возвращает:
    None
    """
    save_data(selected_data, file_path)
