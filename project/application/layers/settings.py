import re
from flet import *

from project.configuration.yolo.data_processing import save_data, load_data
from project.application.backend.cascade_control import reset_settings


def create_settings_layer():
    settings_tab = Tab(text="Settings")

    categories = [
        ("Общие параметры", [
            ("Тип графического устройства", ["cpu", "gpu"]),
            ("Версия YOLO",
             ["yolo11m.pt", "yolo11m-seg.pt", "yolo11l.pt", "yolo11l-seg.pt", "yolo11x.pt", "yolo11x-seg.pt"]),
            ("Кэширование изображений", ["True", "False"])
        ]),
        ("Параметры обучения", [
            ("Количество эпох", [100, 200, 300]),
            ("Контрольные точки обучения", ["True", "False"]),
            ("Детерминированные алгоритмы", ["True", "False"]),
            ("Прямоугольное обучение", ["True", "False"])
        ]),
        ("Параметры ввода/вывода", [
            ("Разовое количество фотографий", r"^\d+$"),
            ("Количество потоков-работников", r"^\d+$"),
            ("Имя директории проекта", r"^[a-zA-Z0-9_-]+$")
        ])
    ]

    settings_container = Column(spacing=10)

    for category, options in categories:
        controls = []
        for label, values in options:
            default = load_data(label)

            if isinstance(values, list):  # Dropdown
                default = default if default in values else "параметр не найден"
                dropdown_setting = Dropdown(
                    label=label,
                    options=[dropdown.Option(str(option)) for option in values],
                    value=str(default),
                    on_change=lambda e: save_data(e.dropdown_setting.value, e.dropdown_setting.label),
                    width=250,
                )
                controls.append(dropdown_setting)
            else:  # TextField
                pattern = values
                textfield_setting = TextField(
                    label=label,
                    value=str(default) if default is not None else "",
                    on_change=lambda e: save_data(e.textfield_setting.value, e.textfield_setting.label)
                    if re.match(pattern, e.textfield_setting.value) else None,
                    width=250,
                )
                controls.append(textfield_setting)

        settings_container.controls.append(ExpansionTile(title=Text(category), controls=controls))

    button_row = Row(
        alignment=MainAxisAlignment.CENTER,
        controls=[
            ElevatedButton(
                "Сбросить настройки",
                on_click=lambda e: reset_settings(settings_container.controls, settings_tab),
                width=200
            )
        ]
    )

    settings_container.controls.append(button_row)
    settings_tab.content = settings_container

    return settings_tab
