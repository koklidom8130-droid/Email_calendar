from datetime import datetime
import time

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

while True:

    now = datetime.now()
    for task in tasks:
        if not task['completed'] and now >= task['time']:
            print( )
            print('Напоминание🤗 ')
            print(f'Задача:{task['title']}')
            print(f'Время:{task['time']}')
            task['completed'] = True
    time.sleep(3)