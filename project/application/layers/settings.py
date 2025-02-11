from flet import *

from project.configuration.yolo.data_processing import save_data, load_data


def create_settings_layer():
    settings_tab = Tab(text="Settings")

    settings_container = Column(
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=50
    )
    default_yolo_device = load_data("Тип графического устройства")
    yolo_device = ["cpu", "gpu"]

    default_yolo_epochs = load_data("Количество эпох")
    yolo_epochs = ["100", "200", "300"]

    default_yolo_image = load_data("Размер изображения")
    yolo_image = ["320", "640", "1280"]

    default_yolo_version = load_data("Версия YOLO")
    yolo_versions = ["yolo11m.pt", "yolo11m-seg.pt", "yolo11l.pt", "yolo11l-seg.pt", "yolo11x.pt", "yolo11x-seg.pt"]
    selection_row = Row(
        alignment=MainAxisAlignment.CENTER,
        controls=[
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Container(width=10),
            Dropdown(
                label="Количество эпох",
                options=[dropdown.Option(version) for version in yolo_epochs],
                value=default_yolo_epochs,
                on_change=lambda e: save_data(int(e.control.value), e.control.label),
                width=300,
            ),
            Container(width=10),
            Dropdown(
                label="Размер изображения",
                options=[dropdown.Option(version) for version in yolo_image],
                value=default_yolo_image,
                on_change=lambda e: save_data(int(e.control.value), e.control.label),
                width=300,
            ),
            Container(width=10),
            Dropdown(
                label="Версия YOLO",
                options=[dropdown.Option(version) for version in yolo_versions],
                value=default_yolo_version,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
            Dropdown(
                label="Тип графического устройства",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: save_data(e.control.value, e.control.label),
                width=300,
            ),
        ]
    )

    settings_container.controls.append(selection_row)
    settings_tab.content = settings_container

    return settings_tab
