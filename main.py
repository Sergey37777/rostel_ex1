import asyncio
from email_sender import EmailSender
from parser import AsyncParser
from data_processing import DataProcessing
from config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL

parser = AsyncParser(
    file_path="inns.txt",
    base_url="https://saby.ru/profile/",
    max_connections=10
)
data = DataProcessing(parser.data)
sender = EmailSender(
    smtp_server=SMTP_SERVER,
    smtp_port=SMTP_PORT,
    sender_email=SENDER_EMAIL,
    sender_password=SENDER_PASSWORD
)

if __name__ == "__main__":
    asyncio.run(parser.run())
    data.create_dataframe()
    data.save_data_as_excel()
    recipient_email = RECIPIENT_EMAIL
    sender.send_email(recipient_email)
