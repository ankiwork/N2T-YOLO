from flet import *

from project.configuration.yolo.data_processing import save_data, load_data


def create_settings_layer():
    settings_tab = Tab(text="Settings")

    settings_container = Column(
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=50
    )

    yolo_device = ["cpu", "gpu"]
    yolo_epochs = ["100", "200", "300"]
    yolo_image = ["320", "640", "1280"]
    yolo_versions = ["yolo11m.pt", "yolo11m-seg.pt", "yolo11l.pt", "yolo11l-seg.pt", "yolo11x.pt", "yolo11x-seg.pt"]
    yolo_bool = ["True", "False"]

    dropdowns = [
        ("Тип графического устройства", yolo_device, load_data("Тип графического устройства")),
        ("Количество эпох", yolo_epochs, load_data("Количество эпох")),
        ("Размер изображения", yolo_image, load_data("Размер изображения")),
        ("Версия YOLO", yolo_versions, load_data("Версия YOLO")),
        ("Контрольные точки обучения", yolo_bool, load_data("Контрольные точки обучения")),
        ("Частота сохранения контрольных точек", list(map(str, range(1, 11))),
         load_data("Частота сохранения контрольных точек")),
        ("Кэширование изображений", yolo_bool, load_data("Кэширование изображений")),
        ("Имя директории проекта", ["Проект1", "Проект2"], load_data("Имя директории проекта")),
        ("Имя тренировочного прогона", ["Запуск1", "Запуск2"], load_data("Имя тренировочного прогона")),
        ("Перезапись существующего названия", yolo_bool, load_data("Перезапись существующего названия")),
        ("Начинать ли обучение с предварительно обученной модели", yolo_bool,
         load_data("Начинать ли обучение с предварительно обученной модели")),
        ("Случайное зерно для обучения", list(map(str, range(0, 1000, 100))),
         load_data("Случайное зерно для обучения")),
        ("Детерминированные алгоритмы", yolo_bool, load_data("Детерминированные алгоритмы")),
        ("Мега класс", yolo_bool, load_data("Мега класс")),
        ("Список классов", ["Класс1", "Класс2"], load_data("Список классов")),
        ("Прямоугольное обучение", yolo_bool, load_data("Прямоугольное обучение"))
    ]

    columns = [Column(spacing=10) for _ in range(4)]

    for i, (label, options, default) in enumerate(dropdowns):
        default = default if default in options else "параметр не найден"

        setting = Dropdown(
            label=label,
            options=[dropdown.Option(str(option)) for option in options],
            value=str(default),
            on_change=lambda e: save_data(e.control.value, e.control.label),
            width=250,
        )
        columns[i % 4].controls.append(setting)

    settings_container.controls.append(Row(spacing=20, controls=columns))
    settings_tab.content = settings_container

    return settings_tab
