from datetime import datetime
import os
import time
import smtplib
import json

task = 'Выполните задачу: '
task_time = datetime(2026,10,7,19,53,)
time_now = datetime.now()

print('___'*50)
print('Моя задача: ')
print('___'*50)
print(f'{task.capitalize()}')
print(f'Выполнить: {task_time}')
print('___'*50)
print()
print(f'Текущее время: {time_now}')

if time_now >= task_time:
    print()
    print('Пора выполнить задачу 😇')
else:
    print()
    print('Время не пришло🙄')
