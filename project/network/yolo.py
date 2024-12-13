from ultralytics import YOLO
from project.configuration.yolo.data_processing import load_data


def start_training():
    results = train_yolo_model()
    print("Обучение завершено. Результаты:", results)


def train_yolo_model():
    """
    Обучает модель YOLO на пользовательском наборе данных.

    Возвращает:
    - results: Результаты обучения.
    """
    # Определение вычислительных модулей
    device = load_data("project/configuration/yolo/data/selected_yolo_device.txt")

    # Определение вычислительных модулей
    epochs = load_data("project/configuration/yolo/data/selected_yolo_epochs.txt")

    # Определение вычислительных модулей
    image = load_data("project/configuration/yolo/data/selected_yolo_image.txt")

    # Загрузка предобученной модели
    model = load_data("project/configuration/yolo/data/selected_yolo_version.txt")
    model = YOLO(model)

    # Определение расположения файла data.yaml
    data_yaml_path = "datasets/data.yaml"

    # Начало обучения на пользовательском наборе данных с сохранением промежуточных результатов
    results = model.train(
        batch=8,
        name="test",
        device=device,
        imgsz=int(image),
        epochs=int(epochs),
        data=data_yaml_path
    )

    return results
