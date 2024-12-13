from project.modules.zip import check_and_create_file

# Определяем путь к файлу для сохранения версии YOLO
yolo_version_path = "project/configuration/yolo/version/selected_yolo_version.txt"


def save_yolo_version(version):
    """
    Сохраняет выбранную версию YOLO в файл.

    Параметры:
    version (str): Выбранная версия YOLO.

    Возвращает:
    None
    """
    # Проверяем и создаем файл, если он не существует
    check_and_create_file("project/configuration/yolo/version/", "selected_yolo_version.txt")

    # Записываем версию в файл
    with open(yolo_version_path, "w") as file:
        file.write(version)


def load_yolo_version():
    """
    Загружает версию YOLO из файла.

    Возвращает:
    str: Содержимое файла или пустую строку, если файл не существует или пуст.
    """
    try:
        with open(yolo_version_path, "r") as file:
            return file.read().strip()

    except FileNotFoundError:
        return ""


def handle_yolo_selection(selected_version):
    """
    Обрабатывает выбор версии YOLO и сохраняет ее в файл.

    Параметры:
    selected_version (str): Выбранная версия YOLO.

    Возвращает:
    None
    """
    save_yolo_version(selected_version)
