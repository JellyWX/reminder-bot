import json
import queue
from RemindMe.Reminder import Reminder

print('Initializing RemindMe::globalvars.py')

calendar = []
todos = {}
timezones = {}

variables = [
    'calendar',
    'todos',
    'timezones'
]

for variable in variables:
    try:
        with open('DATA/{}.json'.format(variable), 'r') as f:
            exec('{} = json.load(f)'.format(variable))

    except FileNotFoundError:
        with open('DATA/{}.json'.format(variable), 'w') as f:
            exec('json.dump({}, f)'.format(variable))
        print('created {} file'.format(variable))

todos = {int(x) : y for x, y in todos.items()}

reminders = queue.PriorityQueue()
[reminders.put(Reminder(dictv=r)) for r in calendar]
