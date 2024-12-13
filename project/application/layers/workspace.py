from flet import *

from project.modules.zip import select_archive
from project.network.yolo import start_training
from project.configuration.yolo.version.processing_version import handle_yolo_selection, load_yolo_version


def create_workspace_layer():
    workspace_tab = Tab(text="Workspace")
    workspace_container = Column()

    default_yolo_version = load_yolo_version()
    yolo_versions = ["yolo11m", "yolo11l", "yolo11x"]

    vertical_space = Container(height=850)
    workspace_container.controls.append(vertical_space)

    dropdown_row = Row(
        alignment=MainAxisAlignment.CENTER,
        controls=[
            Dropdown(
                label="Выберите версию YOLO",
                options=[dropdown.Option(version) for version in yolo_versions],
                value=default_yolo_version,
                on_change=lambda e: handle_yolo_selection(e.control.value),
                width=200,
            )
        ]
    )
    workspace_container.controls.append(dropdown_row)

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
