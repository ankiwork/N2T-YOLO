import os
import shutil
import zipfile
from flet import *

from project.modules.directory import check_and_create_directory


def check_and_create_file(directory, file_name):
    """
    Проверяет существование файла и создает его, если он не существует.

    Параметры:
    Directory (str): Путь к директории, где должен находиться файл.
    File_name (str): Имя файла.

    Возвращает:
    None
    """
    # Формируем полный путь к файлу
    file_path = os.path.join(directory, file_name)

    # Проверка существования файла
    if not os.path.isfile(file_path):
        # Создаем директорию, если она не существует
        os.makedirs(directory, exist_ok=True)

        # Создаем пустой файл
        with open(file_path, 'w') as file:
            file.write("")


def select_archive(workspace_tab, workspace_container):
    """
    Открывает диалог выбора файла для выбора архива.

    Параметры:
    Workspace_tab (Tab): Вкладка рабочего пространства.
    Workspace_container (Column): Контейнер для управления в рабочем пространстве.

    Возвращает:
    None
    """
    # Формирование проводника для выбора файла
    archive_file_picker = FilePicker(on_result=lambda event: handle_file_picker_result(event))
    workspace_container.controls.append(archive_file_picker)
    workspace_tab.update()

    # Вызов проводника
    archive_file_picker.pick_files()


def handle_file_picker_result(event):
    """
    Обрабатывает результат выбора файла.

    Параметры:
    event (FilePickerResultEvent): Результат выбора файла.

    Возвращает:
    None
    """
    if event.files and len(event.files) > 0:
        archive_path = event.files[0].path
        extract_archive(archive_path)


def extract_archive(archive_path):
    """
    Распаковывает ZIP-архив в указанную директорию и перемещает папки train, valid и test.

    Параметры:
    archive_path (str): Путь к архиву.
    target_directory (str): Путь, куда будут перемещены папки train, valid и test.

    Возвращает:
    None
    """

    # Проверка существования архива
    if not os.path.isfile(archive_path):
        return

    archive = os.path.basename(archive_path)
    filename = os.path.splitext(archive)[0]
    # Создание директории для данных, если она не существует
    check_and_create_directory("", filename)

    # Путь к папке datasets
    extract_path = os.path.join(str(filename))

    # Удаление содержимого папки datasets, если она не пуста
    if os.listdir(extract_path):
        shutil.rmtree(extract_path)
        os.makedirs(extract_path)

    # Распаковка архива
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
