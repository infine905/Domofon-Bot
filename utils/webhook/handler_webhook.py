
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils import Database

from config import bot

async def webhookHandler(tenant_id:int, domofon_id:int, apartment_id:int) -> bool:
    chat_id = Database().GetOne(data='tg_id', table_name='Users', find_param='tenant_id', find_value=int(tenant_id))

    message = await bot.send_message(chat_id=int(chat_id), text='Вам позвонили')
    
    messageid = message.message_id
    
    inline_keyboard = [
        [InlineKeyboardButton(text='Открыть', callback_data=f'webhook_open_{tenant_id}_{domofon_id}_{apartment_id}_{messageid}_{chat_id}')]
        [InlineKeyboardButton(text='Закрыть', callback_data='')]
    ]
    message = await bot.send_message(chat_id=int(chat_id), text='Вам позвонили', reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard))