from aiogram import Router
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message

from .profile import getProfile
from utils import getApartments, getDomofons, openDomofon, getDomofonImage
from asyncio import sleep

RouterCallback = Router()

base_text = '🫰 Выберите действие'

@RouterCallback.callback_query()
async def callbackHandler(call:CallbackQuery):
    data = call.data.split('_')
    
    action = data[0]
    inline_keyboard=[]
    
    if action == 'delete':
        await call.message.delete()
        return
    
    if action == 'home':
        await getProfile(call.message, user_id=call.from_user.id)
        return

    if action == 'webhook':
        get_data = data[1]
        tenant_id = data[2]
        domofon_id = data[3]
        apartment_id = data[4]
        messageid = data[5]
        chatid = data[6]
        
        if call.message.photo:                                          # если есть фотка в сообщении
            await call.message.delete()
            message = await call.message.answer(text='✅ Домофон открыт')
            keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

            await nice_sleep(time=3, text='✅ Домофон открыт', message=message, is_del=True)
            
            # await message.edit_text(text=base_text, reply_markup=keyboard)
            return
        
        webhook_text = '✅ Домофон открыт'
        
        await call.bot.edit_message_text(chat_id=chatid, text=webhook_text, message_id=messageid)
        
        await nice_sleep(time=3, text=webhook_text, message=call.message)
        return
        
    #тут action не может быть равен ничему кроме "get"

    get_data = data[1]  

    if get_data == 'apartment':
        tenant_id = int(data[2])
        
        apartments = getApartments(tenant_id=tenant_id)
        
        for apartment in apartments:
            apartment_id = apartment.id
            apartment_name = apartment.name
            apartment_address = apartment.address
            inline_keyboard.append([
                InlineKeyboardButton(text=f'🏠 {apartment_address} кв. {apartment_name}', callback_data=f'get_domofon_{tenant_id}_{apartment_id}')
            ])

        else:
            inline_keyboard.append([
                InlineKeyboardButton(text=f'‹ На главную', callback_data=f'home_{tenant_id}')
            ])
            edit_text = '🪴 *Ваши квартиры:*'

    elif get_data == 'domofon':
        tenant_id = data[2]
        apartment_id = data[3]
        
        domofons = getDomofons(apartment_id=apartment_id, tenant_id=tenant_id)
        
        for domofon in domofons:
            domofon_name = domofon.name
            domofon_id = domofon.id
            
            inline_keyboard.append([
                InlineKeyboardButton(text=f'📱 {domofon_name}', callback_data=f'get_door_{tenant_id}_{domofon_id}')
            ])
            
        else:
            inline_keyboard.append([
                InlineKeyboardButton(text=f'‹ На главную', callback_data=f'home_{tenant_id}')
            ])
            edit_text = '🤙 *Ваши домофоны:*'

    elif get_data == 'door':
        tenant_id = data[2]
        domofon_id = data[3]
        
        inline_keyboard = returnDoorMenu(inline_keyboard=inline_keyboard, tenant_id=tenant_id, domofon_id=domofon_id)
        
        edit_text = base_text

    elif get_data == 'open':
        tenant_id = data[2]
        domofon_id = data[3]
        inline_keyboard = returnDoorMenu(inline_keyboard=inline_keyboard, tenant_id=tenant_id, domofon_id=domofon_id)
        
        if not openDomofon(domofon_id=domofon_id, tenant_id=tenant_id): #если домофон не открылся
            edit_text = '⛔ Домофон недоступен\nПопробуйте позже'

        if call.message.photo:                                          # если есть фотка в сообщении
            await call.message.delete()
            message = await call.message.answer(text='✅ Домофон открыт')
            keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

            await nice_sleep(time=3, text='✅ Домофон открыт', message=message, is_del=False)
            
            await message.edit_text(text=base_text, reply_markup=keyboard)
            return

        else:
            await call.message.edit_text(text='✅ Домофон открыт')
            await nice_sleep(time=3, text='✅ Домофон открыт', message=call.message, is_del=False)        

        edit_text = base_text

    elif get_data == 'img':
        tenant_id = data[2]
        domofon_id = data[3]
        
        photo_url = getDomofonImage(domofon_id=domofon_id, tenant_id=tenant_id)
        if photo_url:
            inline_keyboard = returnDoorMenu(inline_keyboard=inline_keyboard, tenant_id=tenant_id, domofon_id=domofon_id)
            await call.message.edit_media(media=InputMediaPhoto(media=photo_url))
            await call.message.edit_caption(caption=base_text, reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard))
            return

        else:
            await call.message.answer(text='⛔ Камера недоступна')

        returnDoorMenu(tenant_id, domofon_id)

        edit_text = base_text

    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    await call.answer()
    await call.message.edit_text(text=edit_text, reply_markup=keyboard)


def returnDoorMenu(inline_keyboard:list, tenant_id:int, domofon_id:int):
    inline_keyboard.append([
        InlineKeyboardButton(text=f'🔓 Открыть домофон', callback_data=f'get_open_{tenant_id}_{domofon_id}')
    ])
    inline_keyboard.append([
        InlineKeyboardButton(text=f'📸 Получить фотографию', callback_data=f'get_img_{tenant_id}_{domofon_id}')
    ])
    inline_keyboard.append([
        InlineKeyboardButton(text=f'‹ На главную', callback_data=f'home_{tenant_id}')
    ])
    return inline_keyboard


async def nice_sleep(time:int, text:str, message:Message, is_del:bool = True):
    '''
    param: time in seconds
    '''
    print(1)
    digits_with_emojis = (
    (0, "0️⃣"),  # Ноль
    (1, "1️⃣"),  # Один
    (2, "2️⃣"),  # Два
    (3, "3️⃣"),  # Три
    (4, "4️⃣"),  # Четыре
    (5, "5️⃣"),  # Пять
    (6, "6️⃣"),  # Шесть
    (7, "7️⃣"),  # Семь
    (8, "8️⃣"),  # Восемь
    (9, "9️⃣")   # Девять
)
    try:
        for i in range(1, time+1):
            await sleep(1)
            await_text = f'{text} {digits_with_emojis[time+1-i][1]}'
            await message.edit_text(text=await_text)
        else:
            await sleep(1)
            if is_del:
                await message.delete()
        return True
    
    except Exception as e:
        return False
