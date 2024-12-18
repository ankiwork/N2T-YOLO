from flet import *

from project.network.yolo import start_training
from project.modules.files import select_archive
from project.configuration.yolo.version.processing import handle_yolo_selection


def create_workspace_layer():
    workspace_tab = Tab(text="Workspace")
    workspace_container = Column()

    # Кнопка для выбора архива
    select_archive_button = ElevatedButton(
        "Выбрать архив",
        on_click=lambda e: select_archive(workspace_tab, workspace_container)
    )
    workspace_container.controls.append(select_archive_button)

    # Выпадающий список со всеми версиями YOLO
    yolo_versions = ["yolo11m", "yolo11m-seg", "yolo11l", "yolo11l-seg", "yolo11x", "yolo11x-seg"]
    yolo_dropdown = Dropdown(
        label="Выберите версию YOLO",
        options=[dropdown.Option(version) for version in yolo_versions],
        on_change=lambda e: handle_yolo_selection(e.control.value)
    )
    workspace_container.controls.append(yolo_dropdown)

    # Кнопка для начала обучения модели
    train_button = ElevatedButton(
        "Обучить модель",
        on_click=lambda e: start_training()
    )
    workspace_container.controls.append(train_button)
    workspace_tab.content = workspace_container

    return workspace_tab


