from flet import *

from project.application.list import create_layers_list


# TODO: не работает. Добавить обработчик событий в поток.
def toggle_fullscreen(event, page):
    """
    Переключает режим полноэкранного отображения при нажатии клавиши F11.

    Параметры:
    Event (KeyboardEvent): Событие клавиатуры.
    Page (Page): Объект страницы приложения.

    Возвращает:
    None
    """
    if event.key == "F11":
        page.window_full_screen = not page.window_full_screen
        page.update()


def building_the_application(application_page: Page):
    """
    Строит интерфейс приложения, настраивая размеры окна и добавляя вкладки.

    Параметры:
    Application_page (Page): Объект страницы приложения, в которую будут добавлены вкладки.

    Возвращает:
    None
    """
    # Установка размеров окна приложения
    application_page.window_width = 1920
    application_page.window_height = 1080

    # Переключение в полноэкранный режим
    application_page.window_full_screen = True

    # Создание вкладок приложения с заданными параметрами
    application_layers = Tabs(
        expand=1,
        selected_index=0,
        animation_duration=300,
        tabs=create_layers_list()
    )

    # Добавление вкладок на страницу приложения
    application_page.add(application_layers)

    # Добавление обработчика событий клавиатуры
    # application_page.on_keyboard_event = lambda e: toggle_fullscreen(e, application_page)
