from typing import List, Tuple, Dict

import aiohttp
import aiofiles
import asyncio
from lxml import html
from page_selectors import Selectors
import logging


logging.basicConfig(level=logging.DEBUG)


def parse_data(page_content: str):
    """Парсит HTML-страницу и извлекает данные через XPath и CSS-селекторы"""
    tree = html.fromstring(page_content)
    inn = tree.xpath(Selectors.inn)  # ИНН
    kpp = tree.xpath(Selectors.kpp)  # КПП
    ceo_name = tree.cssselect(Selectors.ceo_name)  # ФИО ГД
    position = tree.cssselect(Selectors.position)  # Должность ГД
    phone_number = tree.cssselect(Selectors.phone_number)  # Телефон
    email = tree.cssselect(Selectors.email)  # Email
    website = tree.cssselect(Selectors.website)  # Сайт

    return {
        "inn": inn[0] if inn else "Нет данных",
        "kpp": kpp[0] if kpp else "Нет данных",
        "ceo_name": ceo_name[0].text_content() if ceo_name else "Нет данных",
        "position": position[0].text_content() if position else "Нет данных",
        "phone_number": phone_number[0].text_content() if phone_number else "Нет данных",
        "email": email[0].text_content() if email else "Нет данных",
        "website": website[0].text_content() if website else "Нет данных",
    }


class AsyncParser:
    """Класс для асинхронного получения данных из файла и парсинга страниц"""
    def __init__(self, file_path: str, base_url: str, max_connections: int = 10):
        self.file_path = file_path
        self.base_url = base_url
        self.sem = asyncio.Semaphore(max_connections)  # Ограничение количества одновременных запросов
        self.data = []

    async def fetch(self, session: aiohttp.ClientSession, id_: str) -> Tuple:
        """Асинхронно запрашивает данные по ИНН"""
        async with self.sem:
            url = self.base_url + id_
            async with session.get(url) as response:
                text = await response.text()
                return id_, parse_data(text)

    async def process_ids(self) -> List[Tuple[str, Dict]]:
        """Читает ИНН из файла и выполняет запросы"""
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with aiofiles.open(self.file_path, mode='r') as file:
                tasks = [self.fetch(session, line.strip()) async for line in file]
                return await asyncio.gather(*tasks)

    async def run(self):
        """Запускает процесс обработки ID"""
        results = await self.process_ids()
        self.save_results(results)

    def save_results(self, results):
        """Сохраняет результаты парсинга"""
        for id_, data in results:
            self.data.append(
                {
                    'ИНН': data['inn'],
                    'КПП': data['kpp'],
                    'ФИО ГД': data['ceo_name'],
                    'Должность ГД': data['position'],
                    'Телефон': data['phone_number'],
                    'Email': data['email'],
                    'Сайт': data['website']
                }
            )
        logging.info('Парсинг завершен')
