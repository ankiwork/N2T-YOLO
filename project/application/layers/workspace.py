from flet import *

from project.modules.zip import select_archive
from project.network.yolo import start_training
from project.configuration.yolo.data_processing import handle_data_selection, load_data


def create_workspace_layer():
    workspace_tab = Tab(text="Workspace")
    workspace_container = Column()

    # Тип процессора
    yolo_device_file_path = "project/configuration/yolo/data/selected_yolo_device.txt"
    default_yolo_device = load_data(yolo_device_file_path)
    yolo_device = ["cpu", "gpu"]

    # Количество эпох
    yolo_epochs_file_path = "project/configuration/yolo/data/selected_yolo_epochs.txt"
    default_yolo_epochs = load_data(yolo_epochs_file_path)
    yolo_epochs = ["100", "200", "300"]

    # Размер изображения
    yolo_image_file_path = "project/configuration/yolo/data/selected_yolo_image.txt"
    default_yolo_image = load_data(yolo_image_file_path)
    yolo_image = ["320", "640", "1280"]

    # Версия YOLO
    yolo_version_file_path = "project/configuration/yolo/data/selected_yolo_version.txt"
    default_yolo_version = load_data(yolo_version_file_path)
    yolo_versions = ["yolo11m", "yolo11l", "yolo11x"]

    vertical_space = Container(height=800)
    workspace_container.controls.append(vertical_space)

    selection_row = Row(
        alignment=MainAxisAlignment.CENTER,
        controls=[
            # Тип процессора
            Dropdown(
                label="Тип процессора",
                options=[dropdown.Option(version) for version in yolo_device],
                value=default_yolo_device,
                on_change=lambda e: handle_data_selection(e.control.value, yolo_device_file_path),
                width=300,
            ),

            Container(width=10),

            # Количество эпох
            Dropdown(
                label="Количество эпох",
                options=[dropdown.Option(version) for version in yolo_epochs],
                value=default_yolo_epochs,
                on_change=lambda e: handle_data_selection(e.control.value, yolo_epochs_file_path),
                width=300,
            ),

            Container(width=10),

            # Размер изображения
            Dropdown(
                label="Размер изображения",
                options=[dropdown.Option(version) for version in yolo_image],
                value=default_yolo_image,
                on_change=lambda e: handle_data_selection(e.control.value, yolo_image_file_path),
                width=300,
            ),

            Container(width=10),

            # Версия YOLO
            Dropdown(
                label="Версия YOLO",
                options=[dropdown.Option(version) for version in yolo_versions],
                value=default_yolo_version,
                on_change=lambda e: handle_data_selection(e.control.value, yolo_version_file_path),
                width=300,
            ),
        ]
    )
    workspace_container.controls.append(selection_row)

    fixed_space = Container(height=20)
    workspace_container.controls.append(fixed_space)

    button_row = Row(
        alignment=MainAxisAlignment.CENTER,
        spacing=5,
        controls=[
            ElevatedButton(
                "Выбрать архив",
                on_click=lambda e: select_archive(workspace_tab, workspace_container),
                width=150
            ),

            Container(width=10),

            ElevatedButton(
                "Обучить модель",
                on_click=lambda e: start_training(),
                width=150
            )
        ]
    )
    workspace_container.controls.append(button_row)

    workspace_tab.content = workspace_container

    return workspace_tab
