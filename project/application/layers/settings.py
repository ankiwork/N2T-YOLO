import re
from flet import *

from project.configuration.yolo.data_processing import save_data, load_data


def create_settings_layer():
    settings_tab = Tab(text="Settings")

    settings_container = Row(
        alignment=MainAxisAlignment.CENTER,
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
        ("Кэширование изображений", yolo_bool, load_data("Кэширование изображений")),
        ("Перезапись существующего названия", yolo_bool, load_data("Перезапись существующего названия")),
        ("Начинать ли обучение с предварительно обученной модели", yolo_bool, load_data("Начинать ли обучение с предварительно обученной модели")),
        ("Детерминированные алгоритмы", yolo_bool, load_data("Детерминированные алгоритмы")),
        ("Мега класс", yolo_bool, load_data("Мега класс")),
        ("Прямоугольное обучение", yolo_bool, load_data("Прямоугольное обучение"))
    ]

    input_fields = [
        ("Частота сохранения контрольных точек", load_data("Частота сохранения контрольных точек"), r"^\d+$"),
        ("Случайное зерно для обучения", load_data("Случайное зерно для обучения"), r"^\d+$"),
        ("Имя директории проекта", load_data("Имя директории проекта"), r"^[a-zA-Z0-9_-]+$"),
        ("Имя тренировочного прогона", load_data("Имя тренировочного прогона"), r"^[a-zA-Z0-9_-]+$"),
        ("Список классов", load_data("Список классов"), r"^[a-zA-Z0-9, ]+$")
    ]

    dropdown_column = Column(spacing=10,
                             controls=[],
                             alignment=MainAxisAlignment.CENTER
                             )
    textfield_column = Column(spacing=10,
                             controls=[],
                             alignment=MainAxisAlignment.CENTER
                             )

    for label, options, default in dropdowns:
        default = default if default in options else "параметр не найден"
        setting = Dropdown(
            label=label,
            options=[dropdown.Option(str(option)) for option in options],
            value=str(default),
            on_change=lambda e: save_data(e.control.value, e.control.label),
            width=250,
        )
        dropdown_column.controls.append(setting)

    for label, default, pattern in input_fields:
        text_field = TextField(
            label=label,
            value=str(default) if default else "",
            on_change=lambda e: save_data(e.control.value, e.control.label) if re.match(pattern, e.control.value) else None,
            width=250,
        )
        textfield_column.controls.append(text_field)

    settings_container.controls.append(dropdown_column)
    settings_container.controls.append(textfield_column)
    settings_tab.content = settings_container

    return settings_tab