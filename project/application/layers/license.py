from flet import *


def create_license_layer():
    """
    Создает вкладку "license".

    Параметры:
    None

    Возвращает:
    license_tab: Сформированная вкладка.
    """
    license_tab = Tab(text="License")

    license_container = Column(
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        expand=True
    )

    license_text = (
        "MIT License\n\n"
        "Copyright (c) 2024 Antonov Kirill Alekseevich and Co.\n\n"
        "Permission is hereby granted, free of charge, to any person obtaining a copy "
        "of this software and associated documentation files (the \"Software\"), to deal "
        "in the Software without restriction, including without limitation the rights "
        "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell "
        "copies of the Software, and to permit persons to whom the Software is "
        "furnished to do so, subject to the following conditions:\n\n"
        "The above copyright notice and this permission notice shall be included in all "
        "copies or substantial portions of the Software.\n\n"
        "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR "
        "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, "
        "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE "
        "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER "
        "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, "
        "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE "
        "SOFTWARE."
    )
    log_output = TextField(
        width=900,
        height=460,
        text_size=16,
        color="black",
        multiline=True,
        read_only=True,
        value=license_text
    )
    text_container = Container(
        width=900,
        height=460,
        padding=10,
        border_radius=10,
        alignment=alignment.center,
        border=border.all(1, color="white"),
        content=log_output
    )
    license_container.controls.append(text_container)

    license_tab.content = license_container

    return license_tab
