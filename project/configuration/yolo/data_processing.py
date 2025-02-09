import json

settings_file = "project/configuration/yolo/data/launch_settings.json"

def save_data(data, label):
    """
    Сохраняет данные в файл.

    Параметры:
    data (str): Данные для сохранения в файл;
    label (str): Указатель для записи данных.

    Возвращает:
    None
    """
    with open(settings_file, "w") as f:
        settings = json.load(f)
        if label == "Тип графического устройства":
            settings["selected_yolo_device"] = data
        elif label == "Количество эпох":
            settings["selected_yolo_epochs"] = data
        elif label == "Размер изображения":
            settings["selected_yolo_resolution"] = data
        elif label == "Версия YOLO":
            settings["selected_yolo_version"] = data
        else:
            print("Ошибка типа")
            return
        json.dump(settings, f, indent=4)


def load_data(label):
    """
    Загружает данные из файла.

    Параметры:
    label (str): Указатель для получения данных.

    Возвращает:
    setting (int, str): параметр для настройки
    """
    with open(settings_file, "r") as f:
        settings = json.load(f)
        if label == "Тип графического устройства":
            setting = settings.get("Тип графического устройства")
        elif label == "Количество эпох":
            setting = settings.get("Количество эпох")
        elif label == "Размер изображения":
            setting = settings.get("Размер изображения")
        elif label == "Версия YOLO":
            setting = settings.get("Версия YOLO")
        return setting
