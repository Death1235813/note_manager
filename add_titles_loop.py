from datetime import datetime
from datetime import timedelta
username = input('Имя пользователя: ')
titles = []
content = input('Описание заметки: ')
status = input('Статус заметки: ')
due_date = int(input('Срок выполнения заметки (в днях): ')) # Время до истечения заметки в днях
created_date = datetime.now() # Вводит сегодняшнюю дату компьютера в переменную
issue_date = datetime.now() + timedelta(days = due_date) # Дата окончания заметки
while True:
    title = input('Введите заголовок (для завершения оставьте пустым): ')
    if title != '':
        titles.append(title)
    else:
        break
note = [
username,
content,
status,
str(created_date.day) + '-' + str(created_date.month),
str(issue_date.day) + '-' + str(issue_date.month),
titles
]
print(note)