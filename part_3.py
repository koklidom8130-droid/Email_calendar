from datetime import datetime
import os
import time
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
PASSWORD = os.getenv('PASSWORD')

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 456

'''task- словарь с задачами'''
tasks= [
    {
        'title': 'сделай дз',
        'time': datetime(2026, 10, 14, 19, 30),
        'completed': False
    },
    {
        'title': 'поиграть турнир',
        'time': datetime(2026, 10, 14, 20, 1),
        'completed': False
    },
    {
        'title': 'написать практикум по инфе',
        'time': datetime(2026, 10, 14, 19, 59),
        'completed': False
    }
]

def send_email(task):
    '''Функция отправки сообщения на почту с помощью smtp'''

    message = EmailMessage()
    message ['From'] = EMAIL_ADDRESS
    message['To'] = EMAIL_ADDRESS
    message['Subject'] = 'Напоминание о задачах'

    message.set_content(
        f'Время выполнить задачу\n'
        f'Задача: {task["title"]}\n'
        f'Время: {task["time"]}\n'
    )

    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    server.login(EMAIL_ADDRESS, PASSWORD)
    server.send_message(message)
    server.quit()

    while True:

        now = datetime.now()
        for task in tasks:
            if not task['completed'] and now >= task['time']:
                print()
                print('Напоминание🤗 ')
                send_email(task)

                task['completed'] = True
        time.sleep(3)


