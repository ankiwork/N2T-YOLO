import os


def check_and_create_directory(base_path, folder_name):
    """
    Проверяет, существует ли папка по заданному пути и имени, и создает её, если она не существует.

    Параметры:
    Base_path (str): Путь к родительской папке.
    Folder_name (str): Название создаваемой папки.

    Возвращает:
    None
    """
    # Формирование полного пути к папке
    path = os.path.join(base_path, folder_name)

    if not os.path.exists(path):
        os.makedirs(path)

