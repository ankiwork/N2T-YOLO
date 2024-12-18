import torch
from ultralytics import YOLO
from project.configuration.yolo.version.processing import load_yolo_version


def start_training():
    results = train_yolo_model()
    print("Обучение завершено. Результаты:", results)


def train_yolo_model():
    """
    Обучает модель YOLO на пользовательском наборе данных.

    Возвращает:
    - results: Результаты обучения.
    """
    # Загрузка предобученной модели
    model_name = load_yolo_version()
    model = YOLO(model_name)

    data_yaml_path = "datasets/data.yaml"

    # Установка устройства: 'cuda' для GPU или 'cpu' для CPU
    device = 'cuda' if torch.cuda.is_available() else 'cpu'  # cuda

    # Начало обучения на пользовательском наборе данных
    results = model.train(
        batch=8,
        imgsz=640,
        epochs=10,
        name="test",
        data=data_yaml_path,
        device=device
    )

    return results
