from datetime import datetime
from datetime import timedelta
username = 'Death'
title = 'Начало проекта'
content = 'Второе задание проекта'
status = 'В разработке'
created_date = datetime.now()
issue_date = datetime.now() + timedelta(days = 30)
print('Имя пользователя:',username)
print('Заголовок заметки:',title)
print('Описание заметки:',content )
print('Статус заметки:',status)
print('Дата создания заметки: {}-{}'.format(created_date.day,created_date.month))
print('Дата истечения заметки: {}-{}'.format(issue_date.day,issue_date.month))
