from aiogram import Router
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from .profile import getProfile
from utils import Domofon, Apartment, Tenant

from asyncio import sleep
from requests import get, post
import json
from io import BytesIO

RouterCallback = Router()

@RouterCallback.callback_query()
async def callbackHandler(call:CallbackQuery):
    data = call.data.split('_')
    
    action = data[0]
    
    if action == 'home':
        await getProfile(call.message, user_id=call.from_user.id)
        return

    #тут action не может быть равен ничему кроме "get"
        
    get_data = data[1]  
    inline_keyboard=[]
    
    if get_data == 'apartment':
        tenant_id = int(data[2])
        
        apartments = getApartments(tenant_id=tenant_id)
        
        for apartment in apartments:
            apartment_id = apartment.id
            apartment_name = apartment.name
            
            
            inline_keyboard.append([
                InlineKeyboardButton(text=f'{apartment_name}', callback_data=f'get_domofon_{tenant_id}_{apartment_id}')
            ])

        else:
            inline_keyboard.append([
                InlineKeyboardButton(text=f'На главную', callback_data=f'home_{tenant_id}')
            ])
            mes_text = 'Ваши квартиры'
            
    elif get_data == 'domofon':
        tenant_id = data[2]
        apartment_id = data[3]
        
        domofons = getDomofons(apartment_id=apartment_id, tenant_id=tenant_id)
        
        for domofon in domofons:
            domofon_name = domofon.name
            domofon_id = domofon.id
            
            inline_keyboard.append([
                InlineKeyboardButton(text=f'{domofon_name}', callback_data=f'get_door_{tenant_id}_{domofon_id}')
            ])
            
        else:
            inline_keyboard.append([
                InlineKeyboardButton(text=f'На главную', callback_data=f'home_{tenant_id}')
            ])
            mes_text = 'Ваши домофоны'

    elif get_data == 'door':
        tenant_id = data[2]
        domofon_id = data[3]
        
        inline_keyboard.append([
            InlineKeyboardButton(text=f'Открыть домофон', callback_data=f'get_open_{tenant_id}_{domofon_id}')
        ])
        inline_keyboard.append([
            InlineKeyboardButton(text=f'Получить фотографию', callback_data=f'get_img_{tenant_id}_{domofon_id}')
        ])
        inline_keyboard.append([
            InlineKeyboardButton(text=f'На главную', callback_data=f'home_{tenant_id}')
        ])
        mes_text = 'Выберите действие'

    elif get_data == 'open':
        tenant_id = data[2]
        domofon_id = data[3]

        if not openDomofon(domofon_id=domofon_id, tenant_id=tenant_id):
            mes_text = 'нт'

        await call.message.edit_text(text="Домофон открыт")
        
        await sleep(3)
    
        inline_keyboard.append([
            InlineKeyboardButton(text=f'Открыть домофон', callback_data=f'get_open_{tenant_id}_{domofon_id}')
        ])
        inline_keyboard.append([
            InlineKeyboardButton(text=f'Получить фотографию', callback_data=f'get_img_{tenant_id}_{domofon_id}')
        ])
        inline_keyboard.append([
            InlineKeyboardButton(text=f'На главную', callback_data=f'home_{tenant_id}')
        ])
        mes_text = 'Выберите действие'
            
    
    elif get_data == 'img':
        tenant_id = data[2]
        domofon_id = data[3]
        
        image_bytes = getDomofonImage(domofon_id=domofon_id, tenant_id=tenant_id)
        
        await call.message.answer_photo(photo=image_bytes)

        inline_keyboard.append([
            InlineKeyboardButton(text=f'Открыть домофон', callback_data=f'get_open_{tenant_id}_{domofon_id}')
        ])
        inline_keyboard.append([
            InlineKeyboardButton(text=f'Получить фотографию', callback_data=f'get_img_{tenant_id}_{domofon_id}')
        ])
        inline_keyboard.append([
            InlineKeyboardButton(text=f'На главную', callback_data=f'home_{tenant_id}')
        ])
        mes_text = 'Выберите действие'

    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    await call.answer()
    await call.message.edit_text(text=mes_text, reply_markup=keyboard)
            

def getDomofons(apartment_id:int, tenant_id:int) -> list[Domofon] | None:
    url = f"https://domo-dev.profintel.ru/tg-bot/domo.apartment/{apartment_id}/domofon"
    params  = {
        "tenant_id" : tenant_id
    }
    headers = {
        'x-api-key': 'SecretToken'
    }

    request = get(url=url, headers=headers, params=params )
    
    if request.status_code != 200:
        return None
    
    content = json.loads(request.content.decode())
    
    domofons = []
    for item in content:
        id = item['id']
        name = item['name']
        address = item['location']['readable_address']
        domofons.append(Domofon(id, name, address))
    return domofons
        
        
def getApartments(tenant_id:int) -> list[Apartment] | None:
    url = "https://domo-dev.profintel.ru/tg-bot/domo.apartment"
    params  = {
        "tenant_id": tenant_id
    }
    headers = {
        'x-api-key': 'SecretToken'
    }

    request = get(url=url, headers=headers, params=params )
    
    if request.status_code != 200:
        return None
    
    content = json.loads(request.content.decode())
    apartments = []
    for item in content:
        id = item['id']
        name = item['name']
        address = item['location']['readable_address']
        tenants_data = item.get('tenants', [])
        tenants = [Tenant(t['id']) for t in tenants_data]
        apartments.append(Apartment(id, name, address, tenants))
    return apartments 


def openDomofon(domofon_id:int, tenant_id:int, door_id:int = 0) -> bool:
    url = f"https://domo-dev.profintel.ru/tg-bot/domo.domofon/{domofon_id}/open"
    params  = {
        "tenant_id" : tenant_id
    }
    
    data = {
        "door_id" : door_id
    }
    
    headers = {
        'x-api-key': 'SecretToken'
    }

    request = post(url=url, headers=headers, params=params, json=data)
    
    if request.status_code == 200:
        return True
    
    return False


def getDomofonImage(domofon_id:int, tenant_id:int, media_type:str="JPEG") -> BytesIO | None:
    url = f"https://domo-dev.profintel.ru/tg-bot/domo.domofon/urlsOnType"

    params  = {
        "tenant_id" : tenant_id
    }

    data = {
        "intercoms_id": [
            domofon_id
        ],
        "media_type": [
            "JPEG"
        ]
    }

    headers = {
        'x-api-key': 'SecretToken'
    }

    request = post(url=url, headers=headers, params=params, json=data)
    if request.status_code == 200:
        request_data = json.loads(request.content)
        image_url = request_data[0].get("jpeg")
        image_url_alt = request_data[0].get("alt_jpeg")
        req_image = get(image_url)
        if req_image.status_code == 200:
            image_bytes = BytesIO(req_image.content)
            image_bytes.name = "photo.jpg"
            return image_bytes.read()
        else:
            req_image = get(image_url_alt)
            if req_image.status_code == 200:
                image_bytes = BytesIO(req_image.content)
                image_bytes.name = f"photo_{tenant_id}_{domofon_id}.jpg"
                return image_bytes.read()
    return None