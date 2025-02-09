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


def train_yolo_model():
    """
    Обучает модель YOLO на пользовательском наборе данных.

    Возвращает:
    - results: Результаты обучения.
    """
    # Определение вычислительных модулей
    device = 0 if (load_data("Тип графического устройства")) == 0 else 'cpu'

    # Определение количества эпох
    epochs = load_data("Количество эпох")

    # Определение размера изображения
    image = load_data("Размер изображения")

    # Загрузка предобученной модели
    model = load_data("Версия YOLO")
    model = YOLO(model)

    # Определение расположения файла data.yaml
    data_yaml_path = "datasets/data.yaml"

    # Начало обучения на пользовательском наборе данных с сохранением промежуточных результатов
    results = model.train(
        batch=1,              # Количество изображений, обрабатываемых за один раз
        workers=4,            # Количество потоков-работников для загрузки данных
        patience=5,           # Эпохи ожидания без заметного улучшения
        lr0=0.0001,           # Определяет, насколько быстро модель будет обновлять свои веса
        name="test",          # Имя для текущего запуска обучения
        device=device,        # Устройство для выполнения обучения
        optimizer='SGD',      # Оптимизатор, который следует использовать для обучения
        imgsz=int(image),     # Размер входного изображения
        epochs=int(epochs),   # Количество эпох обучения
        data=data_yaml_path,  # Путь к файлу конфигурации набора данных
    )

    return results
