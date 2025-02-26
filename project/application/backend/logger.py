import io
import re
import threading

progress_chars = [" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]


def grouping(log, match):
    """
        Группирует части строки для удобства.

        Параметры:
        log (LogRedirector) : Объект класса
        match (Match): Отфильтрованная строка

        Возвращает:
            progress_data (dict) : Словарь с группами строки
            progressing (str): Строка полоски прогресса
        """
    progress_data = {
        "epoch": match.group("epoch"),
        "percent": match.group("percent"),
        "cur_iter": int(match.group("cur_iter")),
        "tot_iter": int(match.group("tot_iter")),
        "progress": match.group("progress")
    }

    return progress_data, progressing(log, progress_data.get("cur_iter"), progress_data.get("tot_iter"))


def progressing(self, current_iter, total_iter):
    """
        Обновляет прогресс.

        Параметры:
        self (LogRedirector) : Объект класса
        current_iter (int): Текущий процент выполненных
        total_iter (int): Всего сколько нужно выполнить

        Возвращает:
            (str): Строка полоски прогресса
    """
    progress = current_iter / total_iter if total_iter > 0 else 0
    full_blocks = int(progress * self.bar_length)
    remainder = (progress * self.bar_length - full_blocks) * len(progress_chars)
    partial_block = progress_chars[int(remainder)]

    return "█" * full_blocks + partial_block + "...." * (self.bar_length - full_blocks - 1)


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
        match = re.search(r"(?P<epoch>\d+/\d+).*?:\s*(?P<percent>\d+%)\|.*?\|\s*(?P<cur_iter>\d+)/(?P<tot_iter>\d+) ("
                          r"?P<progress>\[.*?])", message)
        if match:
            parts, progress_bar = grouping(self, match)

            formatted_message = f"{parts.get('epoch')} - {parts.get('percent')}|{progress_bar}| {parts.get('progress')}"

            with self.lock:
                #self.text_widget.value = ""
                self.text_widget.value += "Epoch                     Progress               Remaining time" + "\n"
                self.text_widget.value += formatted_message + "\n"
                self.text_widget.update()
        else:
            self.text_widget.value += message
            self.text_widget.update()

    def flush(self):
        pass
