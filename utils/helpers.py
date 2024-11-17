special_characters = [
    '[',  # Открывающая квадратная скобка
    ']',  # Закрывающая квадратная скобка
    '(',  # Открывающая круглая скобка
    ')',  # Закрывающая круглая скобка
    '~',  # Тильда
    '`',  # Обратная кавычка
    '>',  # Знак больше
    '#',  # Решетка
    '+',  # Плюс
    '=',  # Равно
    '|',  # Вертикальная черта
    '{',  # Открывающая фигурная скобка
    '}',  # Закрывающая фигурная скобка
    '.',  # Точка
    '!',  # Восклицательный знак
]

def Text(text:str):
    return_str = ''
    
    for i, item in enumerate(text):
        if item not in ['-', '*', '_']:
            if item in special_characters:
                return_str += item.replace(item, f'\\{item}')
            else:
                return_str += item
    else:
        return_str = return_str.replace('-*-', '*').replace('-_-', '_')
        return return_str