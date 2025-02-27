import re
from flet import *

from project.application.backend.cascade_control import reset_settings
from project.configuration.yolo.data_processing import save_data, load_data


def create_settings_layer():
    """
    Создает вкладку "settings".

    Параметры:
    None

    Возвращает:
    settings_tab: Сформированная вкладка.
    """
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
        controls = [Container(height=10)]
        for label, values in options:
            default = load_data(label)

            if isinstance(values, list):
                default = default if default in values else "параметр не найден"
                dropdown_setting = Dropdown(
                    label=label,
                    options=[dropdown.Option(str(option)) for option in values],
                    value=str(default),
                    on_change=lambda e: save_data(e.control.value, e.control.label),
                    width=250,
                )
                controls.append(dropdown_setting)

            else:
                pattern = values
                textfield_setting = TextField(
                    label=label,
                    value=str(default) if default is not None else "",
                    on_change=lambda e: save_data(e.control.value, e.control.label) if re.match(pattern, e.control.value) else None,
                    width=250,
                )
                controls.append(textfield_setting)

            controls.append(Container(height=10))

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

    scrollable_container = Container(
        content=Column(
            controls=[settings_container],
            spacing=10,
            scroll=ScrollMode.ALWAYS,
        ),
        expand=True,
    )

    settings_tab.content = scrollable_container

    return settings_tab
