
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils import Database, getApartments, getDomofons
from ..helpers import Text
from config import bot

async def webhookHandler(tenant_id:int, domofon_id:int, apartment_id:int) -> bool | str:
    chat_id = Database().GetOne(data='tg_id', table_name='Users', find_param='tenant_id', find_value=int(tenant_id))
    if not chat_id:
        return False, "User not found"
    
    apartments = getApartments(tenant_id=tenant_id)
  
    for apartment in apartments:
        if apartment.id == apartment_id:
            apartment_name = apartment.address
            break
    else:
        return False, "The user is not a member of the apartment"
    
    domofons = getDomofons(apartment_id=apartment_id, tenant_id=tenant_id)
    for domofon in domofons:
        if domofon.id == domofon_id:
            domofon_name = domofon.name
            break
    else:
        return False, "The intercom is not included in the apartment"
    
    answer_text = f'>🏠 Адрес: {Text(apartment_name)} \n>📲 Домофон: {Text(domofon_name)} \n☎️ Вам поступил звонок'
    
    message = await bot.send_message(chat_id=int(chat_id), text=answer_text)
    
    messageid = message.message_id
    
    inline_keyboard = [
        [InlineKeyboardButton(text='Открыть', callback_data=f'webhook_open_{tenant_id}_{domofon_id}_{apartment_id}_{messageid}_{chat_id}')],
        [InlineKeyboardButton(text='Закрыть', callback_data='delete')]
    ]
    
    await message.edit_text(text=answer_text, reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard))
    
    return True, "Query send success"