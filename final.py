username = input('Введите имя: ')
title = input('Заголовок: ')
title_1 = input('Основная тема: ')
title_2 = input('Номер этапа №')
title_3 = input('Рекомендации для чтения: ')
content = input('Описание: ')
status = input ('Состояние задачи: ')
create_date = input('Дата начала дд.мм.гггг: ')
issue_date = input('Дата окончания: дд.мм.гггг: ')

note = [
    username,title, status, create_date, issue_date,
     [content, title_1,title_2, title_3]
]

print(f'Имя: {username}')
print(f'Заголовк: {title}')
print(f'Состояние задачи: {status}')
print(f'Дата начала: {create_date[:6]}')
print(f'Дата окончания: {issue_date[:6]}')
# print('Заголовки: ', note[:8])
print(f'Заголовки: ', note)