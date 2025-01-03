from datetime import datetime
from datetime import timedelta
due_date = int(input('Срок выполнения заметки (в днях): '))
created_date = datetime.now()
issue_date = datetime.now() + timedelta(days = due_date)
note = [
input('Имя пользователя: '),
input('Описание заметки: '),
input('Статус заметки: '),
str(created_date.day) + '-' + str(created_date.month),
str(issue_date.day) + '-' + str(issue_date.month),
[input('Первый заголовок заметки: '), input('Второй заголовок заметки: '), input('Третий заголовок заметки: ')]
]
print(note)