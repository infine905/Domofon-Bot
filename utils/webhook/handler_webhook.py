
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils import Database, getApartments, getDomofons

from config import bot

async def webhookHandler(tenant_id:int, domofon_id:int, apartment_id:int) -> bool:
    chat_id = Database().GetOne(data='tg_id', table_name='Users', find_param='tenant_id', find_value=int(tenant_id))
    
    apartments = getApartments(tenant_id=tenant_id)
    domofons = getDomofons(apartment_id=apartment_id, tenant_id=tenant_id)
    
    for apartment in apartments:
        apartment_name = apartment.name

    
    
        answer_text = f'''
    >🏠: {apartment_name[1]}
    >📲: {name_domofons}
    ☎️ Вам поступил звонок
        '''
    
    message = await bot.send_message(chat_id=int(chat_id), text=answer_text)
    
    messageid = message.message_id
    
    inline_keyboard = [
        [InlineKeyboardButton(text='Открыть', callback_data=f'webhook_open_{tenant_id}_{domofon_id}_{apartment_id}_{messageid}_{chat_id}')],
        [InlineKeyboardButton(text='Закрыть', callback_data='delete')]
    ]
    
    
    
    await message.edit_text(text=answer_text, reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard))