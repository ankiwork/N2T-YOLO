import os
import time
import json
from functools import wraps


def get_datasets_path():
    """
    Ищет путь до папки с файлами для обучения YOLO

    Возвращает:
    - datasets_path (str): путь до папки с файлами
    """
    # Получаем абсолютный путь к текущему файлу (checks.py)
    current_file = os.path.abspath(__file__)

    # Поднимаемся на три уровня вверх, чтобы попасть в корень проекта
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))

    # Формируем путь к папке datasets
    datasets_path = os.path.join(project_root, "datasets")

    return datasets_path


def retry(num_retries, exception_to_check, sleep_time=0):
    """
    Декоратор, повторяющий выполнение функции обучения, если было вызвано исключение RuntimeError
    """
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, num_retries+1):
                try:
                    path_to_ultralytics = (os.environ['APPDATA'] + "\\Ultralytics\\settings.json")
                    with open(path_to_ultralytics, "r", encoding="utf-8") as f:
                        dataset_path = json.load(f)
                        if dataset_path["datasets_dir"] != get_datasets_path():
                            with open(path_to_ultralytics, "w", encoding="utf-8") as file:
                                dataset_path["datasets_dir"] = get_datasets_path()
                                json.dump(dataset_path, file, indent=0)
                    return func(*args, **kwargs)
                except exception_to_check as e:
                    print(f"{func.__name__} raised {e.__class__.__name__}. Retrying...")
                    if i < num_retries:
                        time.sleep(sleep_time)
            # Raise the exception if the function was not successful after the specified number of retries
            raise exception_to_check
        return wrapper
    return decorate
