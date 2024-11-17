# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# kb = [
#     [InlineKeyboardButton(text='Открыть', callback_data=f'webhook_open_{tenant_id}_{domofon_id}_{apartment_id}_{messageid}_{chat_id}')]
#     [InlineKeyboardButton(text='Закрыть', callback_data='')]
# ]


# digits_with_emojis = (
#     (0, "0️⃣"),  # Ноль
#     (1, "1️⃣"),  # Один
#     (2, "2️⃣"),  # Два
#     (3, "3️⃣"),  # Три
#     (4, "4️⃣"),  # Четыре
#     (5, "5️⃣"),  # Пять
#     (6, "6️⃣"),  # Шесть
#     (7, "7️⃣"),  # Семь
#     (8, "8️⃣"),  # Восемь
#     (9, "9️⃣")   # Девять
# )

# print(digits_with_emojis[1][1])


# for i in range(1,3+1):
#     print(i)

from utils import Database

Database().AddRow(table_name='users', tg_id=1016825585, tenant_id=22051, phone=79604664266)