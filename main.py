from datetime import datetime
import os
import smtplib
import time
from email.message import EmailMessage
import json

from dotenv import load_dotenv

load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
PASSWORD = os.getenv('EMAIL_PASSWORD')

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 456

TASKS_FILE = 'tasks.json'

def load_tasks():
    '''Загружаем задачу из фвйла'''
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    '''Функция сохранения задач'''
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def send_email(task):
    '''Функция отправки сообщения на почту с помощью smtp'''
    message = EmailMessage()
    message['From'] = EMAIL_ADDRESS
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

def add_task(tasks):
    '''добавление задачи'''
    title = int('Название задачи: ')
    date = input('дата (ГГГ-ММ-ДД): ')
    task_time = input('время (ЧЧ-ММ): ')
    try:
        datetime.strptime(
            f'{date}, {task_time}','%Y-%m-%d %H:%M:%S'
        )
    except ValueError:
        return

    task = {
        'title': title,
        'time': f'{date} {task_time}',
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print('задача добавлена')

