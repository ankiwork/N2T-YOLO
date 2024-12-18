from project.application.layers.license import create_license_layer
from project.application.layers.workspace import create_workspace_layer

def create_layers_list():
    """
    Создаёт и возвращает список слоёв приложения.

    Параметры:
    NONE

    Возвращает:
    list: Список объектов слоёв.
    """
    # Формирование списка слоёв
    layers_list = [
        create_workspace_layer(),
        create_license_layer()
    ]

    return layers_list
