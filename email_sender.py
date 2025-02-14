import smtplib
from email.message import EmailMessage
from pathlib import Path
import logging

logging.basicConfig(level=logging.DEBUG)


def get_latest_file() -> Path:
    """Находит последний сохраненный файл Excel в папке"""
    save_dir = Path.home() / "Documents" / "Данные контрагентов"

    # Получаем список всех файлов в папке с расширением .xlsx
    excel_files = list(save_dir.glob("*.xlsx"))

    if not excel_files:
        raise FileNotFoundError("Нет файлов для отправки.")

    # Находим самый свежий файл по дате создания
    latest_file = max(excel_files, key=lambda f: f.stat().st_ctime)
    return latest_file


class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """Инициализация SMTP сервера"""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email: str):
        """Отправляет email с вложением"""
        try:
            file_path = get_latest_file()

            msg = EmailMessage()
            msg["Subject"] = "Данные контрагентов"
            msg["From"] = self.sender_email
            msg["To"] = recipient_email
            msg.set_content("Данные контрагентов во вложении.")

            # Читаем файл и прикрепляем к письму
            with open(file_path, "rb") as file:
                msg.add_attachment(file.read(), maintype="application",
                                   subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                   filename=file_path.name)

            # Отправляем письмо через SMTP
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)

            logging.info(f"Письмо с файлом {file_path.name} отправлено на {recipient_email}")

        except Exception as e:
            logging.error(f"Ошибка при отправке email: {e}")
