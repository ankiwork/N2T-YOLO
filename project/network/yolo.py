from ultralytics import YOLO
from project.configuration.yolo.version.processing_version import load_yolo_version


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

    # device = 'cuda' if torch.cuda.is_available() else 'cpu'

    data_yaml_path = "datasets/data.yaml"

    # Начало обучения на пользовательском наборе данных
    results = model.train(
        batch=16,
        imgsz=640,
        epochs=10,
        name="test",
        data=data_yaml_path,
        device='cpu'
    )

    return results
