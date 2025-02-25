import io
import re
import threading


class LogRedirector(io.TextIOBase):
    """
    Класс для перенаправления вывода в Flet UI на вкладку workspace.

    Параметры:
    TextIOBase (TextField): Текстовое поле для хранения лога обучения

    Возвращает:
        None
    """

    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.lock = threading.Lock()
        self.bar_length = 10

    def write(self, message):
        match = re.search(r"(\d+/\d+).*?:\s*(\d+%)\|.*?\|\s*(\d+)/(\d+) (\[.*?])", message)
        if match:
            epoch_info = match.group(1)  # Например, "1/100"
            percent_complete = match.group(2)  # Прогресс "3%"
            current_iter = int(match.group(3))  # Текущее значение итерации
            total_iter = int(match.group(4))  # Общее количество итераций
            tqdm_progress = match.group(5)  # Часть [00:12<05:44, 1.69s/it]

            progress = current_iter / total_iter if total_iter > 0 else 0

            filled_blocks = int(progress * self.bar_length)  # Количество заполненных блоков
            empty_blocks = self.bar_length - filled_blocks  # Оставшиеся блоки
            progress_bar = "█" * filled_blocks + "." * empty_blocks  # Генерация строки прогресса

            formatted_message = f"{epoch_info} - {percent_complete}|{progress_bar}| {tqdm_progress}"

            with self.lock:
                self.text_widget.value = ""  # Очищаем перед выводом
                self.text_widget.value += "Epoch           Progress       Remaining time" + "\n"
                self.text_widget.value += formatted_message + "\n"
                self.text_widget.update()

    def flush(self):
        pass
