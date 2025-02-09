from project.application.cascade_control import save_settings


# TODO: переделать под работу с json файлом. Поиск осуществлять по ключу.
def save_data(data, label):
    """
    Сохраняет данные в файл.

    Параметры:
    data (str): Данные для сохранения в файл;
    file_path (str): Путь к файлу, в который будут сохранены данные.

    Возвращает:
    None
    """

    save_settings(label)



# TODO: переделать под работу с json файлом. Поиск осуществлять по ключу.
def load_data(file_path):
    """
    Загружает данные из файла.

    Параметры:
    file_path (str): Путь к файлу для загрузки данных.

    Возвращает:
    Str: Содержимое файла или пустую строку, если файл не существует или пуст.
    """
    try:
        with open(file_path, "r") as file:
            return file.read().strip()

    except FileNotFoundError:
        return ""
