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

    # Определение расположения файла data.yaml
    data_yaml_path = "datasets/data.yaml"

    name = load_data("name_of_records_directory")

    batch = load_data("Разовое количество фотографий")

    workers = load_data("Количество потоков-работников")

    patience = load_data("Ожидающие эпохи")

    lr0 = load_data("Скорость обновления весов")

    # Загрузка предобученной модели
    model = load_data("Версия YOLO")
    model = YOLO(model)

    # Начало обучения на пользовательском наборе данных с сохранением промежуточных результатов
    results = model.train(
        batch=int(batch),              # Количество изображений, обрабатываемых за один раз
        workers=int(workers),            # Количество потоков-работников для загрузки данных
        patience=int(patience),           # Эпохи ожидания без заметного улучшения
        lr0=float(lr0),           # Определяет, насколько быстро модель будет обновлять свои веса
        name=name,          # Имя для текущего запуска обучения
        device=device,        # Устройство для выполнения обучения
        optimizer='SGD',      # Оптимизатор, который следует использовать для обучения
        imgsz=int(image),     # Размер входного изображения
        epochs=int(epochs),   # Количество эпох обучения
        data=data_yaml_path,  # Путь к файлу конфигурации набора данных
    )

    return results
