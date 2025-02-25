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

    def write(self, message):
        match = re.search(r"(\d+/\d+).*?:\s*(\d+%)\|.*?\|\s*(\d+/\d+ \[.*?])", message)
        if match:
            epoch_info = match.group(1)  # Например, "1/100"
            percent_complete = match.group(2)  # Прогресс "3%"
            tqdm_progress = match.group(3)  # Часть "6/210 [00:12<05:44,  1.69s/it]"

            filtered_message = f"Эпоха: {epoch_info} - Прогресс: {percent_complete} - {tqdm_progress}"

            with self.lock:
                self.text_widget.value = ""  # Очищаем перед выводом
                self.text_widget.value += filtered_message + "\n"
                self.text_widget.update()
        else:
            self.text_widget.value += message + "\n"
            self.text_widget.update()

    def flush(self):
        pass
