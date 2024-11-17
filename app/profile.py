from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from utils import Database

base_text = '🏠 Добро пожаловать в *Domofon Bot*\! \n✨ Все удобства прямо у вас в Telegram'

async def getProfile(message:Message, is_start:bool = False, user_id:int=None) -> None:
    if not user_id:
        user_id = message.from_user.id

    try:
        tenant_id = Database().GetOne(data='tenant_id', table_name='Users', find_param='tg_id', find_value=user_id)
    except Exception as e:
        print(e)
        return 

    inline_keyboard = [
        [InlineKeyboardButton(text='👀 Мои квартиры', callback_data=f'get_apartment_{tenant_id}')],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

    if is_start:
        await message.answer(text=base_text, reply_markup=keyboard)  
        return

    if message.photo != None:
        await message.delete()
        await message.answer(text=base_text, reply_markup=keyboard)
        return
    
    await message.edit_text(text=base_text, reply_markup=keyboard)
        
    
