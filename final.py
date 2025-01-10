from datetime import datetime
from datetime import timedelta
username = input('Имя пользователя: ')
title1, title2, title3 = input('Первый заголовок заметки: '), input('Второй заголовок заметки: '), input('Третий заголовок заметки: ')
titles = [title1, title2, title3]
content = input('Описание заметки: ')
status = input('Статус заметки: ')
due_date = int(input('Срок выполнения заметки (в днях): '))
created_date = datetime.now()
issue_date = datetime.now() + timedelta(days = due_date)
note = [
username,
content,
status,
str(created_date.day) + '-' + str(created_date.month),
str(issue_date.day) + '-' + str(issue_date.month),
titles
]
print(note)
