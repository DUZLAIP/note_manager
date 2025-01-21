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

print(f'Имя студента: ', note[0])
print(f'Заголовок: ', note[1])
print(f'Основная тема: ', note[5][1])
print(f'Номер этапа: ', note[5][2])
print(f'Рекоментации для чтения: ', note[5][3])
print(f'Описание:', note[5][0])
print(f'Состояние задачи: ', note[2])
print(f'Дата начала: дд.мм.гггг ', note[3][:6])
print(f'Дата окончания: дд.мм.гггг', note[4][:6])