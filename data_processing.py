from typing import List, Dict, Union
import logging
import pandas as pd
from pathlib import Path
from datetime import datetime


logging.basicConfig(level=logging.DEBUG)


def get_save_path():
    """Формирует путь для сохранения файла"""
    save_dir = Path.home() / "Documents" / "Данные контрагентов"  # Каталог сохранения
    save_dir.mkdir(parents=True, exist_ok=True)  # Создаем папку, если её нет

    # Формируем имя файла
    timestamp = datetime.now().strftime("%Y.%m.%d %H-%M-%S")
    file_name = f"{timestamp} Данные контрагентов.xlsx"

    return save_dir / file_name


class DataProcessing:
    def __init__(self, data: List[Dict[str, Union[str, int]]]):
        self.df = None
        self.data = data

    def show_data(self) -> pd.DataFrame:
        return self.df.head()

    def create_dataframe(self) -> None:
        self.df = pd.DataFrame(
            self.data,
            columns=['ИНН', 'КПП', 'ФИО ГД', 'Должность ГД', 'Телефон', 'Email', 'Сайт']
        )

    def save_data_as_excel(self) -> None:
        file_path = get_save_path()  # Получаем путь сохранения
        self.df.to_excel(file_path, index=False)
        logging.info(f'Файл сохранен по пути: {file_path}')
