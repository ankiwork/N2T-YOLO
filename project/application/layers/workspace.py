from flet import *

from project.modules.zip import select_archive
from project.network.yolo import start_training


def create_workspace_layer():
    """
    Создает вкладку "workspace".

    Параметры:
    None

    Возвращает:
    workspace_tab: Сформированная вкладка.
    """
    workspace_tab = Tab(text="Workspace")

    workspace_container = Column(
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=50
    )

    log_output = TextField(
        multiline=True,
        read_only=True,
        max_lines=15,
        width=900,
        height=600
    )

    text_container = Container(
        width=900,
        height=600,
        padding=20,
        border_radius=10,
        alignment=alignment.center,
        border=border.all(1, color="white"),
        content=log_output,
    )
    workspace_container.controls.append(text_container)

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
                on_click=lambda e: start_training(log_output),
                width=150
            )
        ]
    )
    workspace_container.controls.append(button_row)

    workspace_tab.content = workspace_container

    return workspace_tab
