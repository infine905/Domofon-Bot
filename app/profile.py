from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from requests import get, post
import json

from .register import sendContactFromUser
from utils import Database, generateKeyboard, Domofon


async def getProfile(message:Message, is_start:bool = False) -> None:
    try:
        tenant_id = Database().GetOne(data='tenant_id', table_name='Users', find_param='tg_id', find_value=message.from_user.id)
    except:
        await sendContactFromUser(message)
        return
    
    inline_keyboard = [
        [InlineKeyboardButton(text='Мои квартиры', callback_data=f'get_apartment_{tenant_id}')],
        [InlineKeyboardButton(text='Log Out', callback_data='logout')],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    
    if is_start:
        await message.answer(text='Меню', reply_markup=keyboard)  
        return 
    
    await message.edit_text(text='Меню', reply_markup=keyboard)
    
    
def getDofons(apartment_id:int, tenant_id:int) -> list[Domofon] | None:
    url = f"https://domo-dev.profintel.ru/tg-bot/domo.apartment/{apartment_id}/domofon"
    params  = {
        "tenant_id" : tenant_id
    }
    headers = {
        'x-api-key': 'SecretToken'
    }

    request = get(url=url, headers=headers, params=params )
    print(request.status_code)
    print(request.content.decode())
    
    if request.status_code != 200:
        return None
    
    content = json.loads(request.content.decode())
    
    domofons = []
    for item in content:
        id = item['id']
        name = item['name']
        address = item['location']['readable_address']
        print(id, name, address)
        domofons.append(Domofon(id, name, address))


# def a():
    
#     tenat_id = Database().GetOne(data='tenant_id', table_name='Users', find_param='tg_id') #find_value=message.from_user.id
    
#     domofons = getDomofons(tenant_id=tenat_id)
    
#     callbacks = []
#     for i in domofons:
#         domofon_id = int(i['domofon_name'])        
#         callbacks.append(f'{tenat_id}_{domofon_id}')
        
#     inline_keyboard = generateKeyboard(domofons, callbacks)
#     keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)