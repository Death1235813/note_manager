from datetime import datetime
from datetime import timedelta

status = 'В процессе'  # Текущий статус заметки
list_status = ['выполнено', 'в процессе', 'отложено']  # Разрешённые статусы заметки
nomber_status = ['1', '2', '3']  # Разрешённые номера обращения к статусу заметки
print('Текущий статус заметки:', status)
while True:
    status = input('Введите статус заметки (1 - выполнено, 2 - в процессе, 3 - отложено): ')
    if status in nomber_status:
        print('Статус заметки успешно обновлён на:', list_status[int(status) - 1])
        break
    else:
        if status.lower() in list_status:
            print('Статус заметки успешно обновлён на:', status.lower())
            break
        else:
            print(status, 'не может быть статусом заметки')
username = input('Имя пользователя: ')
titles = []
content = input('Описание заметки: ')
due_date = int(input('Срок выполнения заметки (в днях): '))  # Время до истечения заметки в днях
created_date = datetime.now()  # Вводит сегодняшнюю дату компьютера в переменную
issue_date = datetime.now() + timedelta(days = due_date)  # Дата окончания заметки
print('Текущий статус заметки:', status)
while True:
    title = input(
        'Введите заголовок (для завершения оставьте пустым): ')  # Переменная хранящая заголовок введённый пользователем
    if title != '':
        titles.append(title)  # Добавление в список заголовков введённый пользователем заголовок
    else:
        break
note = [
    username,
    content,
    status,
    str(created_date.day) + '-' + str(created_date.month),
    str(issue_date.day) + '-' + str(issue_date.month),
    set(titles)
]
print(note)
