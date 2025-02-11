from ultralytics import YOLO
from project.configuration.yolo.data_processing import load_data
from project.application.cascade_control import update_launch_settings


def start_training():
    """
    Инициирует обучение и контроль за флагом запуска.

    Возвращает:
    None
    """
    results = train_yolo_model()
    update_launch_settings()
    print("Обучение завершено. Результаты:", results)


def params_definition():
    params = {}
    # Определение вычислительных модулей
    device = 0 if (load_data("Тип графического устройства")) == 0 else 'cpu'

    # Определение количества эпох
    epochs = load_data("Количество эпох")

    # Определение размера изображения
    image = load_data("Размер изображения")

    # Определение расположения файла data.yaml
    data_yaml_path = "datasets/data.yaml"
    return params


def train_yolo_model():
    """
    Обучает модель YOLO на пользовательском наборе данных.

    Возвращает:
    - results: Результаты обучения.
    """
    # Загрузка предобученной модели
    model = load_data("Версия YOLO")
    model = YOLO(model)

    # Начало обучения на пользовательском наборе данных с сохранением промежуточных результатов
    results = model.train(params_definition())

    return results
