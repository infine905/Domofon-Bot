from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from utils import Database, generateKeyboard


async def getProfile(message:Message, is_start:bool = False) -> None:
    inline_keyboard = [
        [InlineKeyboardButton(text='Мои квартиры', callback_data='get_apartment')],
        [InlineKeyboardButton(text='Log Out', callback_data='logout')],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    
    if is_start:
        await message.answer(text='Меню', reply_markup=keyboard)  
        return 
    
    await message.edit_text(text='Меню', reply_markup=keyboard)
    
    
def getDomofons(tenant_id) -> list[dict['domofon name':'domofon id']]:
    '''
    вернет список с доступными домофонами
    '''
    pass


# def a():
    
#     tenat_id = Database().GetOne(data='tenant_id', table_name='Users', find_param='tg_id') #find_value=message.from_user.id
    
#     domofons = getDomofons(tenant_id=tenat_id)
    
#     callbacks = []
#     for i in domofons:
#         domofon_id = int(i['domofon_name'])        
#         callbacks.append(f'{tenat_id}_{domofon_id}')
        
#     inline_keyboard = generateKeyboard(domofons, callbacks)
#     keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)