from datetime import datetime
from datetime import timedelta
username = input('Имя пользователя: ')
title1, title2, title3 = input('Первый заголовок заметки: '), input('Второй заголовок заметки: '), input('Третий заголовок заметки: ')
titles = [title1, title2, title3]
content = input('Описание заметки: ')
status = input('Статус заметки: ')
due_date = int(input('Срок выполнения (в днях): '))
created_date = datetime.now()
issue_date = datetime.now() + timedelta(days = due_date)
print('Имя пользователя:', username)
print('Заголовки заметки:', titles)
print('Описание заметки:', content )
print('Статус заметки:', status)
print('Дата создания заметки: {}-{}'.format(created_date.day, created_date.month))
print('Дата истечения заметки: {}-{}'.format(issue_date.day, issue_date.month))