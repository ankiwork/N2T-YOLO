from flet import *

from project.application.list import create_layers_list


def building_the_application(application_page: Page):
    """
    Строит интерфейс приложения, настраивая размеры окна и добавляя вкладки.

    Параметры:
    application_page (Page): Объект страницы приложения, в которую будут добавлены вкладки.

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
