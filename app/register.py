from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from requests import get, post
from config import api_key

RouterReg = Router()


@RouterReg.message(Command('start', 'register'))
async def register(message:Message):
    
    contact_button = [[KeyboardButton(text="Отправить контакт", request_contact=True)]]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=contact_button)
    
    text='Отправьте свой контакт'
    
    await message.answer(text=text, reply_markup=keyboard)
    
@RouterReg.message(F.contact)
async def register(message:Message):
    print(message.contact)
    



def ChekUser(phone):
    data = {
        'phone': phone
    }
    url = "https://domo-dev.profintel.ru/tg-bot/check-tenant"
    
    headers = {
        'x-api-key': api_key
    }
    
    req = post(url=url, headers=headers, data=data)
    print(req)