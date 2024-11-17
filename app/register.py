from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from .profile import getProfile
from utils import Database, getTenantIdByPhone

RouterReg = Router()

text='Отправьте свой контакт'

@RouterReg.message(Command('start'))
async def sendContactFromUser(message:Message) -> None:
    if Database().GetOne(data='id', table_name='Users', find_param='tg_id', find_value=message.from_user.id):
        await getProfile(message=message, is_start=True)
        return
    else:
        contact_button = [[KeyboardButton(text=text, request_contact=True)]]
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=contact_button)
        await message.answer(text=text, reply_markup=keyboard)
        
@RouterReg.message(Command('restore'))
async def sendContactFromUser(message:Message) -> None:
    if Database().GetOne(data='id', table_name='Users', find_param='tg_id', find_value=message.from_user.id):
    
        contact_button = [[KeyboardButton(text=text, request_contact=True)]]
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=contact_button)
        await message.answer(text=text, reply_markup=keyboard)

@RouterReg.message(F.contact)
async def Register(message:Message) -> None:
    if Database().GetOne(data='id', table_name='Users', find_param='tg_id', find_value=message.contact.user_id):
        await message.answer(text='😎 Вы уже зарегистрированы', reply_markup=ReplyKeyboardRemove())
        return
    
    if message.from_user.id != message.contact.user_id:
        await message.answer(text='😡 Отправьте *свой* контакт', reply_markup=ReplyKeyboardRemove())
        return

    phone = message.contact.phone_number.replace(' ', '').replace('+', '')    
    phone = int(phone)
    
    tenant_id = getTenantIdByPhone(phone=phone)

    if tenant_id == False:
        await message.answer(text='😢 Вы не являетесь участником системы')
        return

    if not(Database().AddRow(table_name='users', tg_id=message.from_user.id, tenant_id=tenant_id, phone=phone)):
        text='Не получилось добавить'
        await message.answer(text=text)
        return

    await message.answer(text=f"🎉 Вы успешно авторизировались", reply_markup=ReplyKeyboardRemove())

    await getProfile(message=message, is_start=True)
