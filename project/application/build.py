from flet import *

from project.application.list import create_layers_list


def building_the_application(application_page: Page):
    """
    Строит интерфейс приложения, настраивая размеры окна и добавляя вкладки.

    Параметры:
    Application_page (Page): Объект страницы приложения, в которую будут добавлены вкладки.

    Возвращает:
    None
    """

    def on_window_close(e):
        if e.data == "close":
            application_page.open(confirm_dialog)

    def yes_click(e):
        application_page.window.destroy()

    def no_click(e):
        application_page.close(confirm_dialog)

    confirm_dialog = AlertDialog(
        modal=True,
        title=Text("Подтверждение"),
        content=Text("Вы уверены, что хотите завершить программу"),
        actions=[
            ElevatedButton("Да", on_click=yes_click),
            OutlinedButton("Нет", on_click=no_click),
        ],
        actions_alignment=MainAxisAlignment.END,
    )

    # Установка размеров окна приложения
    application_page.window_width = 1920
    application_page.window_height = 1080
    application_page.window.maximized = True

    # Установка перехвата закрытия программы
    application_page.window.prevent_close = True
    application_page.window.on_event = on_window_close

    # Создание вкладок приложения с заданными параметрами
    application_layers = Tabs(
        expand=1,
        selected_index=0,
        animation_duration=300,
        tabs=create_layers_list(),
    )

    # Добавление вкладок на страницу приложения
    application_page.add(application_layers)
